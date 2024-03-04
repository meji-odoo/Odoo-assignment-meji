# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,fields,api

class fleetCategoriesInherit(models.Model):
    _inherit = 'fleet.vehicle.model.category'

    max_weight = fields.Integer(string='Max Weight(Kg)', default=10)
    max_volume = fields.Integer(string='Max Volume(m\u00B3)', default=10)

    _sql_constraints = [
        ('check_max_volume_positive', 'CHECK(max_volume > 0)', 'Max Volume must be greater than zero!'),
        ('check_max_weight_positive', 'CHECK(max_weight > 0)', 'Max Weight must be greater than zero!')
    ]

    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name}({record.max_weight}kg,{record.max_volume}m\u00B3)"
