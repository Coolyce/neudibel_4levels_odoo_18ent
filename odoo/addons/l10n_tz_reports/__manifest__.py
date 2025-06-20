{
    'name': 'Tanzania - Accounting Reports',
    'countries': ['tz'],
    'version': '1.0',
    'category': 'Accounting/Localizations/Reporting',
    'description': """
Accounting reports for Tanzania
    """,
    'depends': [
        'l10n_tz_account',
        'account_reports',
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
