# -*- coding: utf-8 -*-

import logging 

from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    sacrifice_date = fields.Date(string="Fecha de Sacrificio")
