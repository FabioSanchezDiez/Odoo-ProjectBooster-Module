# -*- coding: utf-8 -*-
# from odoo import http


# class Projectbooster(http.Controller):
#     @http.route('/projectbooster/projectbooster', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/projectbooster/projectbooster/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('projectbooster.listing', {
#             'root': '/projectbooster/projectbooster',
#             'objects': http.request.env['projectbooster.projectbooster'].search([]),
#         })

#     @http.route('/projectbooster/projectbooster/objects/<model("projectbooster.projectbooster"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('projectbooster.object', {
#             'object': obj
#         })
