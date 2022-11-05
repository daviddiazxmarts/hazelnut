
from odoo import models, fields, _


class books_application(models.Model):
    _name = 'books.application'
    _description = 'Categories'
    name = fields.Char(string="Nombre")

    tipo = fields.Selection(
        [
            ('doc', 'World'),
            ('excel', 'Excel'),
            ('power', 'Power Point'),
            ('pdf', 'PDF'),
        ]
    )

    img_documents = fields.Binary(
        string="Imagen"
    )

    def open_view_world(self):
        return {
            'name': _("Documentos"),
            'type': 'ir.actions.act_window',
            'view_mode': 'kanban,form',
            'res_model': 'type.of.document',
            'domain': [('tipo', '=', 'doc')],
            'target': 'current',
        }
    
    def open_view_excel(self):
        return {
            'name': _("Documentos"),
            'type': 'ir.actions.act_window',
            'view_mode': 'kanban,form',
            'res_model': 'type.of.document',
            'domain': [('tipo', '=', 'excel')],
            'target': 'current',
        }
    
    def open_view_power(self):
        return {
            'name': _("Documentos"),
            'type': 'ir.actions.act_window',
            'view_mode': 'kanban,form',
            'res_model': 'type.of.document',
            'domain': [('tipo', '=', 'power')],
            'target': 'current',
        }
    
    def open_view_pdf(self):
        return {
            'name': _("Documentos"),
            'type': 'ir.actions.act_window',
            'view_mode': 'kanban,form',
            'res_model': 'type.of.document',
            'domain': [('tipo', '=', 'pdf')],
            'target': 'current',
            'context': {'create': False, 'edit': False},
        }

class TypeOfDocuments(models.Model):
    _name="type.of.document"
    _description="Type of document"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string="Nombre")
    doc_documents = fields.Binary(
        string="Documento"
    )

    img_document = fields.Binary(
        string="Imagen"
    )

    tipo = fields.Selection(
        [
            ('doc', 'World'),
            ('excel', 'Excel'),
            ('power', 'Power Point'),
            ('pdf', 'PDF'),
        ]
    )

    def action_open_register(self):
        return {
            'name': _("Documentos"),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'type.of.document',
            'target': 'current',
            'res_id': self.id,
        }