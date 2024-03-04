# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Stock Setting',
    'version': '1.0',
    'category': 'Stock',
    'author': 'odoo',
    'sequence': 18,
    'depends': ['stock'],
    'summary': 'The Assignment module',
    'data': [
        'views/res_config_setting_inherit.xml',
    ],
    'auto_install': True,
    'installable': True,
    'license': 'LGPL-3',
}
