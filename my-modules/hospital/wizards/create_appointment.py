# -*- coding: utf-8 -*-

from odoo import models, fields


class CreateAppointment(models.TransientModel):
    _name = 'create.appointment'
    _description = 'Create Appointment Wizard'

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    appointment_date = fields.Date(string="Appointment Date")

    def print_report(self):
        data = {
            'model': 'create.appointment',
            'form': self.read()[0]
        }
        return self.env.ref('hospital.report_appointment').report_action(self, data=data)

    def delete_patient(self):
        for rec in self:
            rec.patient_id.unlink()

    def create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'appointment_date': self.appointment_date,
            'note': 'Created From The Wizard/Code'
        }
        self.patient_id.message_post(body="Creating appointment successfully", subject="Appointment Creation")
        self.env['hospital.appointment'].create(vals)
        
        # new_appointment = self.env['hospital.appointment'].create(vals)
        # context = dict(self.env.context)
        # context['form_view_initial_mode'] = 'edit'
        # return {'type': 'ir.actions.act_window',
        #         'view_type': 'form',
        #         'view_mode': 'form',
        #         'res_model': 'hospital.appointment',
        #         'res_id': new_appointment.id,
        #         'context': context
        #         }

    def get_data(self):
        appointments = self.env['hospital.appointment'].search([])
        print("appointments", appointments)
        for rec in appointments:
            print("Appointment Name", rec.name)
        return{
            "type": "ir.actions.do_nothing"
        }
