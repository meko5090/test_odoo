# -*- coding: utf-8 -*-
from odoo import http

# class CustomerTax(http.Controller):
#     @http.route('/customer_tax/customer_tax/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customer_tax/customer_tax/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customer_tax.listing', {
#             'root': '/customer_tax/customer_tax',
#             'objects': http.request.env['customer_tax.customer_tax'].search([]),
#         })

#     @http.route('/customer_tax/customer_tax/objects/<model("customer_tax.customer_tax"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customer_tax.object', {
#             'object': obj
#         })