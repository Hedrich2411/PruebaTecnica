# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Responsible Invoice',
    'version': '1.1',
    'summary': 'Add a responsible user when generating corrective invoices',
    'depends': ['account'],
    'category': 'Accounting/Accounting',
    'data': [
        'wizard/account_move_reversal_view.xml',
        'views/account_move_view.xml'
    ],
    'installable': True,
    'application': True,
}
