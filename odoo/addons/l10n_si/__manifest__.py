# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Slovenian - Accounting',
    'website': 'https://4levels.co.za/documentation/master/applications/finance/fiscal_localizations.html',
    'icon': '/account/static/description/l10n.png',
    'countries': ['si'],
    'version': '1.1',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
Chart of accounts and taxes for Slovenia.
    """,
    'depends': [
        'account',
        'base_vat',
    ],
    'auto_install': ['account'],
    'data': [
        'data/account_tax_report_data.xml',
    ],
    'demo': [
        'demo/demo_company.xml',
    ],
    'license': 'LGPL-3',
}
