# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': ' Cancel Invoice & Payment ',
    "version": "14.0.1.0.0",
    'description': """
This module helps to cancel invoice & payment.
=============================================

This gives the possibility to update invoice or payment method.
    """,
	"price": 25,
    "currency": "EUR",
    "category": "Invoicing/Sales",
    'license': 'AGPL-3',
    'images': ['static/description/icon.png'],
    "category": "Sale",
    'author': 'Odoo Consultant medconsultantweb@gmail.com',
    'website': 'http://www.weblemon.org',

    'depends': ['sale_management','account'],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'views/inherited_account_move.xml',
        'wizards/wizard_confirm_cancel_payment.xml',
    ],
	'license': 'OPL-1',

}
