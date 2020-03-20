from odoo import http
from odoo.http import request
import json
# from odoo.addons.website_sale.controllers.main import WebsiteSale


# class WebsiteSaleInherit(WebsiteSale):

#     @http.route([
#         '''/shop''',
#         '''/shop/page/<int:page>''',
#         '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>''',
#         '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>/page/<int:page>'''
#     ], type='http', auth="public", website=True)
#     def shop(self, page=0, category=None, search='', ppg=False, **post):
#         res = super(WebsiteSaleInherit, self).shop(page=0, category=None, search='', ppg=False, **post)
#         print("Inherited Odoo Mates ....", res)
#         return res

class Appointment(http.Controller):
    @http.route('/hospital/appointments', type='json', auth='user')
    def appointment_banner(self):
        return {
            'html': """
                <h2><center>testttt bannerrr</center></h2>
            """
        }

class Hospital(http.Controller):

    # Sample Controller Created
    @http.route('/hospital/patient/', website=True, auth='user')
    def hospital_patient(self, **kw):
        # return "Thanks for watching"
        patients = request.env['hospital.patient'].sudo().search([])
        return request.render("hospital.patients_page", {
            'patients': patients
        })

    @http.route('/update_patient', type='json', auth='user')
    def update_patient(self, **rec):
        if request.jsonrequest:
            if rec['id']:
                print("rec...", rec)
                patient = request.env['hospital.patient'].sudo().search([('id', '=', rec['id'])])
                if patient:
                    patient.sudo().write(rec)
                args = {'success': True, 'message': 'Patient Updated'}
        return args

    @http.route('/create_patient', type='json', auth='user')
    def create_patient(self, **rec):
        if request.jsonrequest:
            print("rec", rec)
            if rec['name']:
                vals = {
                    'patient_name': rec['name'],
                    # 'email_id': rec['email_id']
                }
                new_patient = request.env['hospital.patient'].sudo().create(vals)
                print("New Patient Is", new_patient)
                args = {'success': True, 'message': 'Success', 'id': new_patient.id}
        return args

    @http.route('/get_patients', type='json', auth='user')
    def get_patients(self):
        print("Yes here entered")
        patients_rec = request.env['hospital.patient'].search([])
        patients = []
        for rec in patients_rec:
            vals = {
                'id': rec.id,
                'name': rec.patient_name,
                'sequence': rec.name_seq,
            }
            patients.append(vals)
        data = {'status': 200, 'response': patients, 'message': 'Done All Patients Returned'}
        return data

# for test handheld app
class Products(http.Controller):
    @http.route('/get_products', type='json', auth='user')
    def get_products(self):
        print("Yes here enteredYes here enteredYes here enteredYes here enteredYes here entered")
        products_rec = request.env['product.template'].search([])
        products = []
        for rec in products_rec:
            vals = {
                'id': rec.id,
                'default_code': rec.default_code,
                'name': rec.name,
                'list_price': rec.list_price,
                'standard_price': rec.standard_price,
            }
            products.append(vals)
        data = {'status': 200, 'response': products, 'message': 'Success'}
        return data

    @http.route('/create_product', type='json', auth='user')
    def create_product(self, **rec):
        if request.jsonrequest:
            if rec['name']:
                vals = {
                    'default_code': rec['default_code'],
                    'name': rec['name'],
                    'list_price': rec['list_price'],
                    'standard_price': rec['standard_price'],
                }
                new_products= request.env['product.template'].sudo().create(vals)
                args = {'success': True, 'message': 'Create Product Success', 'id': new_products.id}
            return args

    @http.route('/update_product', type='json', auth='user')
    def update_product(self, **rec):
        if request.jsonrequest:
            if rec['id']:
                product = request.env['product.template'].sudo().search([('id', '=', rec['id'])])
                if product:
                    product.sudo().write(rec)
                args = {'success': True, 'message': 'Update Product Success'}
        return args

    @http.route('/delete_product', type='json', auth='user')
    def delete_product(self, **rec):
        if request.jsonrequest:
            if rec['id']:
                product = request.env['product.template'].sudo().search([('id', '=', rec['id'])])
                if product:
                    product.unlink()
                args = {'success': True, 'message': 'Delete Product Success'}
        return args

 