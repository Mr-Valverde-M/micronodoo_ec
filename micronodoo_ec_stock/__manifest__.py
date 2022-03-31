# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Stock Odontology by MICRONODOO S.A.',
    'version': '1.0',
    'summary': 'Ajust module stock for Odontology Center',  #Campo corto de descripción del módulo
    'description': """
        Funcionalidades:
            - Agrega nuevos campos al módulo de inventario en Odoo V.14
            - Modifica ciertos métodos nativos de inventario.
            - Modifica permisos por perfiles de usuario.
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
        'stock', 
    ],
    #'data': [
    #    'views/res_company_view.xml'
    #],
    #'demo': [
    #    ''
    #],
    'auto_install': False,
    'installable': True,
    'application': False,
}