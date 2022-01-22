# -*- encoding: UTF-8 -*-
#Modify by Ing. Manuel Valverde M.
{
    'name': 'Extra Information in Contact',
    'version': '14.0.1',
    'summary': 'This module will allow you to add additional information to the contact file',
    'description':"""
        - You will add a Marital status field
    """,
    'category': 'Contacts',
    'author': 'MicronOdoo',
    'maintainer':'MicronOdoo', #Ing. Manuel Valverde
    'website': 'https://nanoits.odoo.com',
    'license': 'AGPL-3',
    'contributors': [
        'Manuel Valverde M',
    ],
    'depends': [
        'base', 'contacts',
    ],
    'images':'static/description/icon.png',
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