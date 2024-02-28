from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Expense(models.Model):
    _name = 'projectbooster.expense'

    EXPENSE_TYPES = [
        ('travel', 'Viaje'),
        ('materials', 'Materiales'),
        ('services', 'Servicios'),
        ('other', 'Otro'),
    ]

    name = fields.Char(string="Nombre del Gasto", required=True)

    description = fields.Text(string="Descripción")

    expense_value = fields.Float(string="Coste del Gasto", digits=(10, 2))
    
    expense_type = fields.Selection(EXPENSE_TYPES, string="Tipo de Gasto")
    
    project_ids = fields.Many2many('projectbooster.project', string="Proyectos Relacionados")

    @api.constrains('expense_value')
    def _check_expense_value(self):
        for expense in self:
            if expense.expense_value < 0:
                raise ValidationError("El valor del gasto no puede ser negativo.")