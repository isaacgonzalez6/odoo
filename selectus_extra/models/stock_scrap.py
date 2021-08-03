# -*- coding: utf-8 -*-

import logging 

from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class StockScrap(models.Model):
    _inherit = 'stock.scrap'

    scrap_reason = fields.Text(string="Motivo de Desecho")
