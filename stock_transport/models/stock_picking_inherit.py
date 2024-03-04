# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class stockPickingInherit(models.Model):
    _inherit = "stock.picking"

    weight = fields.Float("Weight ", compute='_compute_weight')
    volume = fields.Float("Volume ", compute='_compute_volume')

    @api.depends('move_ids')
    def _compute_volume(self):
        for record in self:
            volume = map(lambda move_id: move_id.product_id.volume * move_id.quantity, record.move_ids)
            record.volume = sum(volume)

    @api.depends('move_ids')
    def _compute_weight(self):
        for record in self:
            weight = map(lambda move_id: move_id.product_id.weight * move_id.quantity, record.move_ids)
            record.weight = sum(weight)
