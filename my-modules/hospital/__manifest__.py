# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': "Module for manage the hospitals",

    'description': """
        Long description of module's purpose
    """,

    'author': "srank meng",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'sale', 'board', 'report_xlsx'],

    # always loaded
    'data': [
        # 'data/data.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'reports/appointment.xml',
        'reports/report.xml',
        'reports/patient_card.xml',
        'reports/sale_report_inherit.xml',
        'wizards/create_appointment.xml',
        'views/appointment.xml',
        'views/patient.xml',
        'views/dashboard.xml',
        'views/doctor.xml',
        'views/lab.xml',
        'views/settings.xml',
        'views/menu.xml',
        'views/templates.xml',
        'views/sale_order.xml',
        'data/cron.xml',
        'data/sequence.xml',
        'data/mail_template.xml',
           
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
