# -*- coding: utf-8 -*-
{
    'name': "Hazelnut",
    'description': """
        La Aplicacion es util para nutriologos, docentes y estudihambres,
        ya que contiene diversos Documentos y formatos que se puede emplear
        en distintas situaciones :DD xD
    """,

    'author': "Hazelnut",
    'category': 'Libros',
    'version': '15.0',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'demo': [
        'demo/demo.xml',
    ],
}
