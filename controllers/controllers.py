# -*- coding: utf-8 -*-
from odoo import http

# class RamcarMonitoring(http.Controller):
#     @http.route('/ramcar_monitoring/ramcar_monitoring/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ramcar_monitoring/ramcar_monitoring/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ramcar_monitoring.listing', {
#             'root': '/ramcar_monitoring/ramcar_monitoring',
#             'objects': http.request.env['ramcar_monitoring.ramcar_monitoring'].search([]),
#         })

#     @http.route('/ramcar_monitoring/ramcar_monitoring/objects/<model("ramcar_monitoring.ramcar_monitoring"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ramcar_monitoring.object', {
#             'object': obj
#         })