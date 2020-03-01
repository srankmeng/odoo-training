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
    'depends': ['base', 'mail', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        # 'data/data.xml',
        'data/cron.xml',
        'data/sequence.xml',
        'data/mail_template.xml',
        'wizards/create_appointment.xml',
        'views/patient.xml',
        'views/appointment.xml',
        'views/doctor.xml',
        'views/lab.xml',
        'views/templates.xml',
        'views/settings.xml',
        'reports/appointment.xml',
        'reports/report.xml',
        'reports/patient_card.xml',
        'reports/sale_report_inherit.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
