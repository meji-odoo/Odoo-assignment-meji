# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,fields,api
from odoo.exceptions import ValidationError

class stockPickingBatchInherit(models.Model):
    _inherit = 'stock.picking.batch'

    dock_id = fields.Many2one('stock.dock', string='Dock')
    vehical = fields.Many2one('fleet.vehicle', string='Vehichal')
    vehical_category = fields.Many2one('fleet.vehicle.model.category', string='Vehical Category')
    weight = fields.Float(string='Weight', compute='_compute_weight', store=True)
    volume = fields.Float(string='Volume', compute='_compute_volume', store=True)

    @api.depends('vehical_category', 'picking_ids', 'move_line_ids.product_id.weight')
    def _compute_weight(self):
        for record in self:
            if record.vehical_category:
                record.weight = (sum(picking.weight for picking in record.picking_ids) / record.vehical_category.max_weight * 100)

    @api.depends('vehical_category', 'picking_ids', 'move_line_ids.product_id.volume')
    def _compute_volume(self):
        for record in self:
            if record.vehical_category:
                record.volume = (sum(picking.volume for picking in record.picking_ids) / record.vehical_category.max_volume * 100)


    # these is for name to display in gantt view but is also effect in form view so below code is for learning purpose
    # def _compute_display_name(self):
    #     display_name_temp = super()._compute_display_name()
    #     for record in self:
    #         if record.vehical_category and record.vehical.driver_id:
    #             record.display_name = f"{record.vehical_category.max_weight}kg,{record.vehical_category.max_volume}m\u00B3,{record.vehical.driver_id.name}"
    #         elif record.vehical_category:
    #             record.display_name = f"{record.vehical_category.max_weight}kg,{record.vehical_category.max_volume}m\u00B3"
    #         else:
    #             return display_name_temp

