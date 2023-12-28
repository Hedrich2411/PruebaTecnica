# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Stock report',
    'version': '1.1',
    'summary': 'consolidated balance of physical stock available for each warehouse',
    'depends': ['stock'],
    'category': 'Inventory/Inventory',
    'data': [
        'stock_report.xml',
    ],
    'installable': True,
    'application': True,
}
