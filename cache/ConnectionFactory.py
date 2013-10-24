from pymongo import *

class ConnectionFactory:
    print "Conectando al Servidor de Base de Datos Local..."
    conexion = Connection() # Se crea la conexion con la base de datos de mongo, en este caso se usa la url
    db = conexion.linkedinAppCache # El nombre de nuestra base de datos.

    def getCollection(self, entity):

        if entity.getCollectionName() == 'Companies':
            return self.db.Companies
        elif entity.getCollectionName() == 'Person':
            return self.db.Person
        elif entity.getCollectionName() == 'Location':
            return self.db.Location
        else:
            return None


