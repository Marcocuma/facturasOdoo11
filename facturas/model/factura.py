#-*- coding: utf-8 -*-

from odoo import models, fields, api

class Dato(models.Model):
	_name = 'facturas.factura'
	idfactura = fields.Char('Id factura', required=True)
	empresa = fields.Char('Empresa',required=True)
	telefono = fields.Integer('Telefono',required=True)
	cliente = fields.Many2one('facturas.cliente','Cliente')
	producto = fields.Many2many('facturas.producto',"many2many_default")


