# Copyright 2019 Marcelo Frare (Ass. PNLUG - Gruppo Odoo <http://odoo.pnlug.it>)
# Copyright 2019 Stefano Consolaro (Ass. PNLUG - Gruppo Odoo <http://odoo.pnlug.it>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    "name":     "Management System - Action Template",
    "summary":  "Add Template management for Actions.",
    "version":  "12.0.1.0.0",
    "development_status" : "Beta",

    "author":   "Associazione PNLUG - Gruppo Odoo, Odoo Community Association (OCA)",

    "website":  "https://github.com/OCA/management-system",
    "license":  "AGPL-3",

    "category": "Management System",
    "depends": ['mgmtsystem_action',
                'mgmtsystem_nonconformity',
                ],
    "data":    ['views/mgmtsystem_action_views.xml',
                'views/mgmtsystem_nonconformity_views.xml',
                ],
    'installable': True,
}
