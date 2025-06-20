# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Netherlands - Accounting',
    'icon': '/account/static/description/l10n.png',
    'countries': ['nl'],
    'version': '3.3',
    'category': 'Accounting/Localizations/Account Charts',
    'author': 'Onestein (http://www.onestein.eu)',
    'website': 'https://4levels.co.za/documentation/master/applications/finance/fiscal_localizations/netherlands.html',
    'depends': [
        'base_iban',
        'base_vat',
        'account',
    ],
    'auto_install': ['account'],
    'data': [
        'data/account_account_tag.xml',
        'data/account_tax_report_data.xml',
        'views/res_config_settings_view.xml',
    ],
    'demo': [
        'demo/demo_company.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
