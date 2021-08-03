# -*- coding: utf-8 -*-

{
    'name': 'selectus_extra',
    'version': '1.0',
    'description': 'Modulo para cambiar configuraciones para Selectus',
    'author': 'Meridasoft',
    'category': 'third-party',
    'depends': [
        'base',
        'product',
        'product_expiry',
        'stock',
        'mrp',
    ],
    'data': [
        'views/product_template_view.xml',
        'views/res_partner_view.xml',
        'views/stock_crap_view.xml',
        'views/stock_picking_view.xml',
        'views/stock_move_view.xml',
        'views/mrp_unbuild.xml',
        'views/mrp_production.xml',
        'reports/addenda_liverpool.xml',
    ],
    'auto_install': True,
    'application': True,
    'installable': True,
}
