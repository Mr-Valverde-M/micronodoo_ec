# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Contacts Odontology by MICRONODOO S.A.',
    'version': '1.0',
    'summary': 'Ajust module contacts for Odontology Center',  #Campo corto de descripción del módulo
    'description': """
        Funcionalidades:
            - Agrega nuevos campos a los contactos en Odoo V.14
            - Modifica ciertos métodos nativos
        Autor:    
            - Ing. Manuel Valverde M.
    
    """, #Campo largo en la descripción del módulo
    'author': 'MICRONODOO S.A.',
    'maintainer': 'MICRONODOO S.A.',
    'website': 'www.micronodoo.com',
    'license': 'OEEL-1',
    'category': 'Odontology',
    'depends': [
        'base',
        'l10n_ec', 
    ],
    #'data': [
    #    'views/res_company_view.xml'
    #],
    #'demo': [
    #    ''
    #],
    'auto_install': True,
    'installable': True,
    'application': False,
}