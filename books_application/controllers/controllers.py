# -*- coding: utf-8 -*-
# from odoo import http


# class BooksApplication(http.Controller):
#     @http.route('/books_application/books_application', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/books_application/books_application/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('books_application.listing', {
#             'root': '/books_application/books_application',
#             'objects': http.request.env['books_application.books_application'].search([]),
#         })

#     @http.route('/books_application/books_application/objects/<model("books_application.books_application"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('books_application.object', {
#             'object': obj
#         })
