from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one("stock.transport.dock", string="Dock")
    vehicle_id = fields.Many2one("fleet.vehicle", string="Vehicle")
    vehicle_category_id = fields.Many2one(
        "fleet.vehicle.model.category", string="Vehicle Category"
    )
    total_weight = fields.Float(
        string="Total Weight", compute="_compute_product_weight_volume", store=True
    )
    total_volume = fields.Float(
        string="Total Volume", compute="_compute_product_weight_volume", store=True
    )
    weight_percentage = fields.Float(
        string="Weight Percentage", compute="_compute_product_weight_volume", store=True
    )
    volume_percentage = fields.Float(
        string="Volume Percentage", compute="_compute_product_weight_volume", store=True
    )

    @api.depends("move_line_ids.product_id", "move_line_ids.quantity")
    def _compute_product_weight_volume(self):
        for batch in self:
            total_weight = 0.0
            total_volume = 0.0
            for move_line in batch.move_line_ids:
                total_weight += move_line.product_id.weight * move_line.quantity
                total_volume += move_line.product_id.volume * move_line.quantity
            batch.total_weight = total_weight
            batch.total_volume = total_volume
            if batch.vehicle_category_id:
                max_weight = batch.vehicle_category_id.max_weight
                max_volume = batch.vehicle_category_id.max_volume

                if total_weight <= max_weight:
                    batch.weight_percentage = (total_weight / max_weight) * 100.0

                if total_volume <= max_volume:
                    batch.volume_percentage = (total_volume / max_volume) * 100.0
                    