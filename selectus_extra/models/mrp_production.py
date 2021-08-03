# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    total_unbuild = fields.Integer(string="Deconstrucción", compute="_get_unbuild_orders")

    def button_unbuild(self):
        self.ensure_one()
        return {
            'name': _('Unbuild: %s', self.product_id.display_name),
            'view_mode': 'form',
            'res_model': 'mrp.unbuild',
            'view_id': self.env.ref('mrp.mrp_unbuild_form_view_simplified').id,
            'type': 'ir.actions.act_window',
            'context': {'default_product_id': self.product_id.id,
                        'default_mo_id': self.id,
                        'default_company_id': self.company_id.id,
                        'default_location_id': self.location_dest_id.id,
                        'default_location_dest_id': self.location_src_id.id,
                        'default_lot_id': self.lot_producing_id.id,
                        'create': False, 'edit': False},
            'domain': {'lot_id': [('id','=',[16])]},
            'target': 'new',
        }

    @api.depends()
    def _get_unbuild_orders(self):
        for rec in self:
            mrp_unbuild = self.env['mrp.unbuild'].search([('mo_id','=', self.id)])
            self.total_unbuild = len(mrp_unbuild)

    def action_view_unbuild(self):
        return {
            'name': _('Ordenes de deconstruccion: %s', self.name),
            'view_mode': 'tree',
            'res_model': 'mrp.unbuild',
            'view_id': self.env.ref('mrp.mrp_unbuild_tree_view').id,
            'type': 'ir.actions.act_window',
            'domain': [('mo_id','=',self.id)],
            'target': 'current',
        }
