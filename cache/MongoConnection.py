from ConnectionFactory import *

from django.core import serializers
import json
class MongoConnection:
    
    factory = ConnectionFactory()
    
    def saveCompnay(self, company):
        self.db.Companies.insert(company.__dict__)
        
    def savePerson(self,person):
        self.db.Persons.insert(person.__dict__)
        
    def saveLocation(self,location):
        self.db.Locations.insert(location.__dict__)

    def save(self, Object):
        coll = self.factory.getCollection(Object)
        coll.insert(Object.__dict__)
        
    def printConnection(self):
        print "base de datos"

    
    

   
   
    
