# -*- coding: utf-8 -*-
{
    'name': "4levelsBot - HR",
    'summary': """Bridge module between hr and mailbot.""",
    'description': """This module adds the 4levelsBot state and notifications in the user form modified by hr.""",
    'website': "https://4levels.co.za/app/discuss",
    'category': 'Productivity/Discuss',
    'version': '1.0',
    'depends': ['mail_bot', 'hr'],
    'installable': True,
    'auto_install': True,
    'data': [
        'views/res_users_views.xml',
    ],
    'license': 'LGPL-3',
}
