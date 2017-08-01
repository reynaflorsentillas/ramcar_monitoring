from odoo import models, fields, api

class AndroidUser(models.Model):
    _name = 'android.user'
    _description = 'Android User'
    _inherits = {'res.partner': 'partner_id'}
    order = 'name, username'

    # def _default_groups(self):
    #     default_user = self.env.ref('base.default_user', raise_if_not_found=False)
    #     return (default_user or self.env['android.user']).sudo().groups_id

    partner_id = fields.Many2one('res.partner', required=True, ondelete='restrict', auto_join=True, string='Related Partner', help='Partner-related data of the user')

    # name = fields.Char(required=True)
    username = fields.Char(required=True)
    password = fields.Char(required=True)
    active = fields.Boolean(default=True)
    info = fields.Text(string='Extra info')

    # groups_id = fields.Many2many('res.groups', 'res_groups_android_users_rel', 'uid', 'gid', string='Groups')

    employee_ids = fields.One2many('hr.employee', 'android_user_id', string='Related Employees')
    
    # @api.model
    # def create(self, vals):
    #     groups_proxy = self.env['res.groups']
    #     group_ids = groups_proxy.search([('name', '=', 'Android User')])
    #     vals['groups_id'] = [(6, 0, group_ids)]
    #     return super(AndroidUser, self).create(vals)
