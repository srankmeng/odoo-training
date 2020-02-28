# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Appointment'
    _order = 'appointment_date desc'
    
    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        result = super(HospitalAppointment, self).create(vals)
        return result

    def _get_default_note(self):
        return 'just default note'

    name = fields.Char(string='Appointment ID', required=True, copy='false', readonly=True, index=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    patient_age = fields.Integer('Age', related='patient_id.patient_age')
    note = fields.Text(string="Registration Note", default=_get_default_note)
    doctor_note = fields.Text(string="Note")
    pharmacy_note = fields.Text(string="Note")
    appointment_lines = fields.One2many('hospital.appointment.lines', 'appointment_id', string='Appointment Lines')
    appointment_date = fields.Date(string="Date", required=True)
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='Status', required=True, default='draft')

class HospitalAppointmentLines(models.Model):
    _name = 'hospital.appointment.lines'
    _description = 'Appointment Lines'


    product_id = fields.Many2one('product.product', string='Medicine')
    product_qty = fields.Integer(string='Quantity')
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment ID')
   