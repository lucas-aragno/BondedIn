from ConnectionFactory import *

from django.core import serializers
import json
class MongoConnection:
    
    factory = ConnectionFactory()
    

    def save(self, Object):
        coll = self.factory.getCollection(Object.getCollectionName())
        coll.insert(Object.__dict__)
        
    def find(self, collectionName, search):
        coll = self.factory.getCollection(collectionName)
        return coll.find()
