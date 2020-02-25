# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    patient_name = fields.Char(string='Patient Name')
    # patient_name = fields.selection('hospital_patient','Patient Name')

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient record'
    _rec_name = 'patient_name'

    patient_name = fields.Char(string='Name', required=True)
    patient_age = fields.Integer('Age')
    note = fields.Text(string="Note")
    image = fields.Binary(string="Image")
    name_seq = fields.Char(string='Order Refrence', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patience.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result


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
