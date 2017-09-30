# -*- coding: utf-8 -*-
###############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2017 Humanytek (<www.humanytek.com>).
#    Manuel Márquez <manuel@humanytek.com>
#    Rubén Bravo <rubenred18@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################


from openerp import fields, api, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    product_tmpl_max_qty_total = fields.Float(
        compute='_compute_product_tmpl_max_qty_total',
        string='Total quantity of products for max template',
        help='Total quantity of products for the product template most added'
            'in order lines.')

    @api.depends('order_line.product_qty')
    def _compute_product_tmpl_max_qty_total(self):

        for order in self:
            total_qty_per_tmpl = dict()
            qty_total = 0.0

            for line in order.order_line:
                tmpl_id_str = line.product_id.product_tmpl_id.id
                if tmpl_id_str not in total_qty_per_tmpl.keys():
                    total_qty_per_tmpl[tmpl_id_str] = line.product_qty
                else:
                    total_qty_per_tmpl[tmpl_id_str] += line.product_qty
            
            order.product_tmpl_max_qty_total = max(total_qty_per_tmpl.values())

    @api.multi
    def button_confirm(self):
        super(PurchaseOrder, self).button_confirm()

        for order in self:

            if order.company_id.po_double_validation == 'one_step'\
                    or (order.company_id.po_double_validation == 'two_step'\
                        and order.product_tmpl_max_qty_total <
                        self.env.user.company_id.po_double_validation_product_tmpl_qty)\
                    or order.user_has_groups('purchase.group_purchase_manager'):
                order.button_approve()
            else:
                order.write({'state': 'to approve'})

        return {}
