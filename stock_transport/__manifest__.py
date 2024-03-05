{
    "name": "Transport Management System",
    "version": "1.2",
    "summary": "transport",
    "sequence": 10,
    'depends': ['base','mail','stock_picking_batch', 'fleet'],
    "description": """
        Easy to use Stock Transport App
    """,
    "category": "Accounting/Transport Management System",
    "application": True,
    "data": [
        "security/ir.model.access.csv",
        "views/stock_picking_batch_views.xml",
        "views/fleet_vehicle_model_category_views.xml",
    ],
}
