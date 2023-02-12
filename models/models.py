# -*- coding: utf-8 -*-

from odoo import models, fields, api



class modulo3_modeloActores(models.Model):
     _name = 'modulo3.modelo'
     _description = 'Modulo Actores de un VideoClub'

     name = fields.Char(string='Nombre y Apellidos del actor ',help='Nombre completo',required=True)
     year = fields.Char(string='Año de Nacimiento',help='Año',size=4)
     description =  fields.Text(string='Descripcion del actor')

class modulo2_modeloCategorias(models.Model):
     _name = 'modulo2.modelo'
     _description = 'Modulo Categorias de un VideoClub'

     name = fields.Selection(string='Categoria', selection =[('Comedia', 'Comedia'), 
     ('Drama', 'Drama'),('Terror','Terror'),('Ciencia Ficcion','Ciencia Ficcion'),('Aventura','Aventura')])
     description =  fields.Text(string='Descripcion')

class modulo_modeloPelicula(models.Model):
     _name = 'modulo1.modelo'
     _description = 'Modulo Pelicula de un VideoClub'

     name = fields.Char(string='Título de la pelicula',help='Título',required=True)
     year = fields.Char(string='Año',help='Año',size=4)
     reserved_movie = fields.Boolean(string='Pelicula Alquilada')
     sales = fields.char(string='Total Ventas',compute='_una_funcion')
     photo = fields.Image(max_with =250,max_height=250) 
     last_login = fields.Datetime(
         string='Ultimo acceso',
         required=True        
     )
     categoria_id = fields.Many2one(
         string='Categoria',
         comodel_name='modulo2.modelo',
         ondelete='restrict',
     )

     def _una_funcion(self):
         for record in self:
             record.sales = '135000'






     
 #description = fields.Text()

 #@api.depends('value')
# def _value_pc(self):
         #for record in self:
             #record.value2 = float(record.value) / 100
