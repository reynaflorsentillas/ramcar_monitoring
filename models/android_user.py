from odoo import models, fields, api

class AndroidUsers(models.Model):
    _name = 'ramcar.monitoring.android.users'

    name = fields.Char(required=True)
    username = fields.Char(required=True)
    password = fields.Char(required=True)

    employee_ids = fields.fields.One2many('hr.employee', 'android_user_id', string='Related Employees')
