# -*- coding: utf-8 -*-
{
    'name': "Ramcar Monitoring",

    'summary': """
        Monitoring of Field Engineers and Deliveries""",

    'description': """
        Backend for Ramcar's monitoring of field engineers and deliveries.
    """,

    'author': "Capstone Solutions Inc.",
    'website': "http://www.capstone.ph",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'project'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/ramcar_monitoring_security.xml',
        'data/ir_sequence_data.xml',
        'views/android_user_views.xml',
        'views/hr_employee_views.xml',
        'views/field_report_view.xml',
        'views/delivery_report_view.xml',
        'views/menu_views.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}