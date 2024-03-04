# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Dispatch Mmanagement System',
    'version': '1.0',
    'category': 'Fleet',
    'author': 'odoo',
    'sequence': 18,
    'depends': ['fleet', 'stock', 'stock_picking_batch'],
    'summary': 'The Assignment module',
    'data': [
        'security/ir.model.access.csv',

        'data/stock_dock_data.xml',

        'views/fleet_categories_inherit.xml',
        'views/stock_picking_inherit.xml',
        'views/stock_batch_transfer_inherit.xml',
        'views/stock_dock_view.xml',
        'views/stock_dock_menu.xml',
    ],
    'auto_install': True,
    'installable': True,
    'license': 'LGPL-3',
}
