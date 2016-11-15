# -*- coding: utf-8 -*-
{
    'name': "Módulo de Ejemplo",

    'summary': """Manage trainings""",

    'description': """
        Módulo01 for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "Alvaro Villavicencio Ramírez",
    'website': "http://www.soluciones4gcom",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
}
