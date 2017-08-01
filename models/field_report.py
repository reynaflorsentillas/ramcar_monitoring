from odoo import models, fields, api, _

class FieldReport(models.Model):
    _name = 'field.report'
    _description = 'Field Engineer Report Form'

    name = fields.Char('Field Report Reference',default=lambda self: _('New Report'), copy=False, required=True)

    status = fields.Selection([
        ('new', 'New'), 
        ('ongoing', 'Ongoing'),
        ('done', 'Done')], default='new', string='Status')

    partner_id = fields.Many2one('res.partner', 'Customer', index=True, help='Choose partner for whom the order will be invoiced and delivered.')
    # address_id = fields.Many2one('res.partner', 'Delivery Address', domain="[('parent_id','=',partner_id)]")
    default_address_id = fields.Many2one('res.partner', string='Address/Location', compute='_compute_default_address_id')

    project_id = fields.Many2one('project.project', 'Project', required=True)
    project_site_address = fields.Text('Project Site Address')

    contact_person_id = fields.Many2many('res.partner', string='Site Contact Person', required='True',  ondelete='cascade')
    jobsite_contact_number = fields.Char(string='Job Site Telephone or Mobile Number', required='True')

    accomplished_by = fields.Many2one('android.user', 'Accomplished By',  ondelete='cascade')

    @api.one
    @api.depends('partner_id')
    def _compute_default_address_id(self):
        if self.partner_id:
            self.default_address_id = self.partner_id.address_get(['contact'])['contact']

    @api.model
    def create(self, values):
        if values.get('name', _('New Report')) == _('New Report'):
            values['name'] = self.env['ir.sequence'].next_by_code('field.report')
        result = super(FieldReport, self).create(values)
        return result

