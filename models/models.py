# -*- coding: utf-8 -*-

from odoo import models, fields, api

class modulo2_modeloCategorias(models.Model):
     _name = 'modulo2.modelo'
     _description = 'Modulo Categorias de un VideoClub'

     name = fields.Selection(string='Categoria', selection =[('valor1', 'Comedia'), 
     ('valor2', 'Drama'),('valor3','Terror'),('valor4','Ciencia Ficcion'),('valor5','Aventura')])
     description =  fields.Text(string='Descripcion')

class modulo_modeloPelicula(models.Model):
     _name = 'modulo1.modelo'
     _description = 'Modulo Pelicula de un VideoClub'

     name = fields.Char(string='Título de la pelicula',help='Título',required=True)
     year = fields.Char(string='Año',help='Año',size=4)
     reserved_movie = fields.Boolean(string='Pelicula Alquilada')
     sales = fields.Integer(string='Total Ventas')
     
     categoria_id = fields.Many2one(
         string='Categoria',
         comodel_name='modulo2.modelo',
         ondelete='restrict',
     )
     
 #description = fields.Text()

 #@api.depends('value')
# def _value_pc(self):
         #for record in self:
             #record.value2 = float(record.value) / 100
