# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,fields,api

class stockDock(models.Model):
    _name = 'stock.dock'

    _sql_constraints = [
        ('name_uniq', 'UNIQUE (name)', 'Dock name must be unique')
    ]

    name = fields.Char(required=True)
    sequence = fields.Integer()
