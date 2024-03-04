from odoo import models, fields, api


class StockTransportDock(models.Model):
    _name = "stock.transport.dock"
    _description = "Stock Transport Dock"

    name = fields.Char(string="Name", required=True)
    dock_ids = fields.One2many("stock.picking.batch", "dock_id", string="Docks")