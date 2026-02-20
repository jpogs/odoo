from odoo import models, fields, api

class PosOrder(models.Model):
    _inherit = "pos.order"

    table_start_time = fields.Datetime("Table Start Time")
    table_end_time = fields.Datetime("Table End Time")

    table_duration = fields.Float(
        "Table Duration (Minutes)",
        compute="_compute_table_duration",
        store=True,
    )

    @api.depends("table_start_time", "table_end_time")
    def _compute_table_duration(self):
        for order in self:
            if order.table_start_time and order.table_end_time:
                delta = order.table_end_time - order.table_start_time
                order.table_duration = delta.total_seconds() / 60
            else:
                order.table_duration = 0
