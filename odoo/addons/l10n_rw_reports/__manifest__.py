{
    'name': 'Rwanda - Accounting Reports',
    'version': '1.0',
    'category': 'Accounting/Localizations/Reporting',
    'description': """
Accounting reports for Rwanda
    """,
    'depends': [
        'l10n_rw', 'account_reports'
    ],
    'data': [
        "data/balance_sheet.xml",
        "data/profit_loss.xml",
    ],
    'installable': True,
    'auto_install': True,
    'website': 'https://4levels.co.za/app/accounting',
    'license': 'OEEL-1',
}
