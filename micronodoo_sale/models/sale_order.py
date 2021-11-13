# -*- encoding: UTF-8 -*-
#Modify by Ing. Manuel Valverde M.

from odoo import api, fields, models

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

margin = fields.Float(
    string = 'Margin',
    compute = '_compute_margin',
    digits = 'Product Price',
    store = True,
    groups = 'base.group_user',
    readonly = False)

margin_percent = fields.Float(
    string = 'Margin (%)',
    compute = '_compute_margin',
    store = True,
    groups = 'base.group_user',
    readonly = False,
    )
