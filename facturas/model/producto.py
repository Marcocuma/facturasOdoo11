# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Dato(models.Model):
    _name = 'facturas.producto'
    idproducto = fields.Integer('Id producto', required=True)
    nombre = fields.Char('Nombre', required=True)
    precio = fields.Float('Precio', required=True)

    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res
