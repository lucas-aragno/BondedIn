from pymongo import *

from django.core import serializers
import json
class Conexion:
    
    
    print "Conectando al Servidor de Base de Datos Local..."
    conexion = Connection() # Se crea la conexion con la base de datos de mongo, en este caso se usa la url
    db = conexion.linkedinAppCache # El nombre de nuestra base de datos.
    
    def saveCompnay(self, company):
        self.db.Companies.insert(company.__dict__)
        
    def savePerson(self,person):
        self.db.Persons.insert(person.__dict__)
        
    def saveLocation(self,location):
        self.db.Locations.insert(location.__dict__)
        
        
    def printConnection(self):
        print "base de datos"

    
    

   
   
    