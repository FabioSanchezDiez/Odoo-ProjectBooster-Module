# -*- coding: utf-8 -*-
{
    'name': "Project Booster",

    'summary': """
        Sistema de gestión de proyectos.""",

    'description': """
        Sistema de gestión de proyectos para llevar un buen seguimiento de los mismo.
    """,

    'author': "Fabio Sánchez Diez",
    'website': "https://projectbooster.000webhostapp.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Gestión',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/project.xml',
        'views/task.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'application':True,
    'sequence':1
}
