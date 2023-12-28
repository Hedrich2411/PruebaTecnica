# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Partner Invoices',
    'version': '1.1',
    'summary': 'Add the relationship between invoices and Partner in the Partner view',
    'depends': ['account','contacts'],
    'data': [
        'views/res_partner.xml'
    ],
    'installable': True,
    'application': True,
}
