# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': '4levelsBot',
    'version': '1.2',
    'category': 'Productivity/Discuss',
    'summary': 'Add 4levelsBot in discussions',
    'website': 'https://4levels.co.za/app/discuss',
    'depends': ['mail'],
    'auto_install': True,
    'installable': True,
    'data': [
        'views/res_users_views.xml',
        'data/mailbot_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'mail_bot/static/src/scss/odoobot_style.scss',
        ],
    },
    'license': 'LGPL-3',
}
