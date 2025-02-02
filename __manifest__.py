{
    'name': 'Committee Management',
    'version': '17.0.0.1',
    'summary': 'Manage Organizing Committees and Advisory Boards',
    'description': 'Module to manage Organizing Committees and Advisory Boards with members.',
    'author': 'Md. Shaheen Hossain',
    'website': 'https://eagle-erp.com',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'views/committee_views.xml',
        'views/board_views.xml',
        'views/member_views.xml',
    ],
    'installable': True,
    'application': True,
}