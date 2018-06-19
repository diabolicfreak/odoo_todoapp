from odoo import models, fields

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'ToDo Task'
    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
    date_deadline = fields.Date('Deadline')
    user_id = fields.Many2one(
        'res.users', 
        string='Responsible',
        default=lambda self: self.env.user
    )
    team_ids = fields.Many2many(
        'res.partner',
        string='Teams'
    )
