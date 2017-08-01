from odoo import models, fields, api

class hr_employee(models.Model):
    _inherit = ['hr.employee']

    android_user_id = fields.Many2one('android.user')
    