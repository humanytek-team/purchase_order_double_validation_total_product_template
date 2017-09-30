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

from openerp import fields, models
from openerp.tools.translate import _


class Company(models.Model):
    _inherit = 'res.company'

    po_double_validation_product_tmpl_qty = fields.Float(
        string=u'Limit by total quantity of products per template',
        default=20,
        help="Minimum quantity total of products per template for which a "
            "double validation is required")
