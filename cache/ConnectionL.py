from pymongo import *
from Company import Company
from django.core import serializers
import json
class Conexion:
    
    print "Conectando al Servidor de Base de Datos Local..."
    conexion = Connection() # Se crea la conexion con la base de datos de mongo, en este caso se usa la url
    db = conexion.linkedinAppCache # El nombre de nuestra base de datos.
    

    company= Company()
    company.setId(234)
    db.Companies.insert({"id":1})
    db.Companies.insert(serializers.serialize('json',company))
    

   
   
    