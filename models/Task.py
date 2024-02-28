from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class Task(models.Model):
    _name = 'projectbooster.task'
    
    name = fields.Char(string="Nombre de la tarea", required=True)

    description = fields.Text(string="Descripción")

    date = fields.Date(string="Fecha de finalización")

    completed = fields.Boolean(string="Completada", default=False, help="Marca si la tarea está completa o no")

    project_id = fields.Many2one('projectbooster.project', ondelete='cascade', string="Proyecto")

    collaborators_ids = fields.Many2many('res.partner', string="Colaboradores")

    days_remaining = fields.Integer(string="Días Restantes", compute='_compute_days_remaining', store=True)

    @api.depends('date', 'completed')
    def _compute_days_remaining(self):
        for task in self:
            if not task.completed and task.date:
                today = fields.Date.from_string(datetime.today().strftime('%Y-%m-%d'))
                task.days_remaining = (fields.Date.from_string(task.date) - today).days
            else:
                task.days_remaining = None

    @api.constrains('date')
    def _check_date_not_past(self):
        for task in self:
            if task.date and not task.completed and task.date < fields.Date.today():
                raise ValidationError("La fecha no puede ser anterior al día actual a menos que la tarea esté completada.")