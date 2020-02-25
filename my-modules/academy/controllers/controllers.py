# -*- coding: utf-8 -*-
# from odoo import http

from odoo import http
import json

class Academy(http.Controller):

    @http.route("/academy/academy/", auth='none', type='http',method=['GET'])
    def index(self, **kw):

        Teachers = http.request.env['academy.teachers']
        data = {
            'teachers': Teachers.search([])
        }
        print(data)

        headers = {'Content-Type': 'application/json'}
        body = { 'results': { 'code':200, 'message':'OK'}}

        return http.Response(json.dumps(body), headers=headers)


    # @http.route('/academy/academy/', auth='public', website=True)
    # def index(self, **kw):
    #     Teachers = http.request.env['academy.teachers']
    #     return http.request.render('academy.index', {
    #         'teachers': Teachers.search([])
    #     })

    # @http.route('/academy/<model("academy.teachers"):teacher>/', auth='public', website=True)
    # def teacher(self, teacher):
    #     return http.request.render('academy.biography', {
    #         'person': teacher
    #     })


# class Academy(http.Controller):
#     @http.route('/academy/academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/academy/academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy.listing', {
#             'root': '/academy/academy',
#             'objects': http.request.env['academy.academy'].search([]),
#         })

#     @http.route('/academy/academy/objects/<model("academy.academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy.object', {
#             'object': obj
#         })
