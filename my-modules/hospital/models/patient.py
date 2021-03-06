# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    patient_name = fields.Char(string='Patient Name')
    # patient_name = fields.selection('hospital_patient','Patient Name')

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient record'
    _rec_name = 'patient_name'

    def action_patients(self):
        print('ssssssssssssssssssssssssssss')
        return {
            'name': _('Patient Server Action'),
            'domain': [], 
            'view_type': 'form',
            'res_model': 'hospital.patient',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def print_report(self):
        return self.env.ref('hospital.report_patient_card').report_action(self)

    @api.model
    def test_cron_job(self):
        print("""
            =============
            test cron job
            =============
        """)
    
    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s - %s' % (rec.name_seq, rec.patient_name)))
        return res

    @api.constrains('patient_age')
    def check_age(self):
        for rec in self:
            if rec.patient_age <= 5:
                raise ValidationError(_('The age must be greater than 5'))

    @api.depends('patient_age')
    def set_age_group(self):
        self.age_group = 'major'
        for rec in self:
            if rec.patient_age:
                if rec.patient_age < 18:
                    rec.age_group = 'minor'

    def get_appointment_count(self):
        count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])
        self.appointment_count = count
                    
    def open_patient_appointment(self):
        return {
            'name': _('Appointments'),
            'domain': [('patient_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'hospital.appointment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    @api.onchange('doctor_id')
    def set_doctor_gender(self):
        for rec in self:
            if rec.doctor_id:
                rec.doctor_gender = rec.doctor_id.gender

    def action_send_card(self):
        template_id = self.env.ref('hospital.patient_card_email_template').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)

    @api.depends('patient_name')
    def _compute_upper_name(self):
        for rec in self:
            rec.patient_name_upper = rec.patient_name.upper() if rec.patient_name else False

    def _inverse_upper_name(self):
        for rec in self:
            rec.patient_name = rec.patient_name_upper.lower() if rec.patient_name_upper else False

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patience.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result

    patient_name = fields.Char(string='Name', required=True, track_visibility='always')
    patient_age = fields.Integer('Age', track_visibility='always', group_operator=False)
    patient_age2 = fields.Integer('Age2')
    note = fields.Text(string="Note")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], default='male', string="Gender")
    age_group = fields.Selection([
        ('major', 'Major'),
        ('minor', 'Minor')
    ], string='Age Group', compute='set_age_group', store=True)
    image = fields.Binary(string="Image", attachment=True)
    name_seq = fields.Char(string='Patient Code', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    email_id = fields.Char(string="Email")
    user_id = fields.Many2one('res.users', string="PRO")
    appointment_count = fields.Integer('Appointment', compute='get_appointment_count')
    active = fields.Boolean('Active', default=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    doctor_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string="Doctor Gender")
    patient_name_upper = fields.Char(compute='_compute_upper_name', inverse='_inverse_upper_name')


# from odoo import models, fields, api


# class hospital(models.Model):
#     _name = 'hospital.hospital'
#     _description = 'hospital.hospital'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
