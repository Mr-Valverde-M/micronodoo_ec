# -*- encoding: UTF-8 -*-
#Modify by Ing. Manuel Valverde M.
{
    'name': 'Digit Margin in Sale',
    'version': '0.1',
    'summary': 'This module will allow adding analytical accounts in the delivery or exit orders',
    'category': 'Ventas',
    'author': 'MicronOdoo',
    'maintainer':'MicronOdoo', #Ing. Manuel Valverde
    'website': 'https://nanoits.odoo.com',
    'license': 'AGPL-3',
    'contributors': [
        'Manuel Valverde M',
    ],
    'depends': [
        'base', 'sale_management', 'sale_stock_margin', 'sale_margin', 'product_margin',
    ],
    #'external_dependencies': {
    #    'python': [
    #        '',
    #    ],
    #},
    #'data': [
    #    'views/stock_picking_form_inherit.xml',
    #],
    'installable': True,
    'auto_install': False,
    'application': False,
}