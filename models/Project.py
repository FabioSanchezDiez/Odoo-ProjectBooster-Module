from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Project(models.Model):
    _name = 'projectbooster.project'

    name = fields.Char(string="Nombre del proyecto", required=True)

    description = fields.Text(string="Descripción")

    project_icon = fields.Image(string="Icono", help="Icono para el curso")

    duration_days = fields.Integer(string="Duracion estimada (Días)")

    category = fields.Char(string="Categoria")

    extra_information = fields.Text("Información Extra")

    user_id = fields.Many2one('res.users', ondelete='set null', string="Usuario")
    
    task_ids = fields.One2many('projectbooster.task', 'project_id', string="Tareas")

    @api.constrains('duration_days')
    def _check_duration_days(self):
        for project in self:
            if project.duration_days < 0:
                raise ValidationError("La duración estimada no puede ser negativa.")
            
            