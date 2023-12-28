# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Email Transfer',
    'version': '1.1',
    'summary': 'Send messages to users according to a transfer',
    'depends': ['stock','mail'],
    'category': 'Inventory/Inventory',
    'data': [
        'views/stock_picking.xml',
        'wizard/send_note_picking_view.xml'
    ],
    'installable': True,
    'application': True,
}
