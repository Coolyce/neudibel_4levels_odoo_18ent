# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Turkey - Accounting Reports',
    'version': '1.0',
    'category': 'Accounting/Localizations/Reporting',
    'description': """
Accounting reports for Turkey
    """,
    'depends': [
        'l10n_tr', 'account_reports'
    ],
    'data': [
        'data/account_report_tr_balance_sheet_data.xml',
        'data/account_report_tr_pnl_data.xml',

        'views/account_journal_views.xml',
        'views/product_view.xml',
    ],
    'installable': True,
    'auto_install': True,
    'website': 'https://4levels.co.za/app/accounting',
    'license': 'OEEL-1',
}
