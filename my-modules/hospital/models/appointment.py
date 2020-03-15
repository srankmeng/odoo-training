# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Appointment'
    _order = 'appointment_date desc'
    
    def action_notify(self):
        for rec in self:
            rec.doctor_id.related_user.notify_danger('Appointmenttt')

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'
            return {
                'effect': {
                    'fadeout': 'slow',
                    'message': 'Confirmed ... Thank you',
                    'type': 'rainbow_man',
                }
            }

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def delete_lines(self):
        for rec in self:
            print('rec', rec)
            rec.appointment_lines = [(5, 0, 0)]

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        result = super(HospitalAppointment, self).create(vals)
        return result
    
    def write(self, vals):
        # overriding the write method of appointment model
        res = super(HospitalAppointment, self).write(vals)
        print("Test write function, Test write function, Test write function, Test write function, ")
        return res

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        for rec in self:
            return {'domain': { 'order_id': [('partner_id', '=', rec.partner_id.id)]}}

    @api.model
    def default_get(self, fields):
        res = super(HospitalAppointment, self).default_get(fields)
        print("test......")
        res['patient_id'] = 1
        res['note'] = 'Default value note'
        return res
        

    # def _get_default_note(self):
    #     return 'just default note'

    name = fields.Char(string='Appointment ID', required=True, copy='false', readonly=True, index=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    patient_age = fields.Integer('Age', related='patient_id.patient_age')
    amount = fields.Integer('Amount')
    note = fields.Text(string="Registration Note")
    # note = fields.Text(string="Registration Note", default=_get_default_note)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    doctor_note = fields.Text(string="Note")
    pharmacy_note = fields.Text(string="Note")
    appointment_lines = fields.One2many('hospital.appointment.lines', 'appointment_id', string='Appointment Lines')
    appointment_date = fields.Date(string="Date")
    # appointment_date_end = fields.Date(string="Date End")
    partner_id = fields.Many2one('res.partner', string="Partner")
    order_id = fields.Many2one('sale.order', string="Sale order")
    product_id = fields.Many2one('product.template', string="Product Template")
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='Status', required=True, default='draft')

    @api.onchange('product_id')
    def onchange_product_id(self):
        for rec in self:
            lines = [(5, 0, 0)]
            # lines = []
            for line in self.product_id.product_variant_ids:
                val = {
                    'product_id': line.id,
                    'product_qty': 15
                }
                lines.append((0, 0, val))
            rec.appointment_lines = lines

class HospitalAppointmentLines(models.Model):
    _name = 'hospital.appointment.lines'
    _description = 'Appointment Lines'


    product_id = fields.Many2one('product.product', string='Medicine')
    product_qty = fields.Integer(string='Quantity')
    sequence = fields.Integer(string='Sequence')
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment ID')
   