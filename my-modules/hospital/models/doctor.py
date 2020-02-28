# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Doctor record'
    _rec_name = 'name'

    
    code = fields.Char(string='Doctor Code', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    name = fields.Char(string='Name', required=True, track_visibility='always')
    age = fields.Integer('Age', track_visibility='always')
    note = fields.Text(string="Note")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], default='male', string="Gender")
    related_user = fields.Many2one('res.users', string='Related User')

    @api.model
    def create(self, vals):
        if vals.get('code', _('New')) == _('New'):
            vals['code'] = self.env['ir.sequence'].next_by_code('hospital.doctor.sequence') or _('New')
        result = super(HospitalDoctor, self).create(vals)
        return result

