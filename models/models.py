from odoo import models, fields, api
from odoo.exceptions import ValidationError

# https://spilymp.github.io/ibo/

class Project(models.Model):
    _name = 'projectbooster.project'

    name = fields.Char(string="Nombre del proyecto", required=True)
    description = fields.Text(string="Descripción")
    project_icon = fields.Image(string="Icono", help="Icono para el curso")
    duration_days = fields.Integer(string="Duracion estimada (Días)")
    category = fields.Char(string="Categoria")
    extra_information = fields.Text("Información Extra")
    user_id = fields.Many2one('res.users', ondelete='set null', string="User")
    task_ids = fields.One2many('projectbooster.task', 'project_id', string="Tareas")


    @api.constrains('duration_days')
    def _check_duration_days(self):
        for project in self:
            if project.duration_days < 0:
                raise ValidationError("La duración estimada no puede ser negativa.")


class Task(models.Model):
    _name = 'projectbooster.task'
    
    name = fields.Char(string="Nombre de la tarea", required=True)
    description = fields.Text(string="Descripción")
    date = fields.Date(string="Fecha")
    completed = fields.Boolean(string="Completada", default=False, help="Marca si la tarea está completa o no")

    project_id = fields.Many2one('projectbooster.project', string="Proyecto", required=True)
    collaborators_ids = fields.Many2many('res.partner', string="Colaboradores")


# class projectbooster(models.Model):
#     _name = 'projectbooster.projectbooster'
#     _description = 'projectbooster.projectbooster'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
