from pymongo import *

class ConnectionFactory:
    print "Conectando al Servidor de Base de Datos Local..."
    conexion = Connection() # Se crea la conexion con la base de datos de mongo, en este caso se usa la url
    db = conexion.linkedinAppCache # El nombre de nuestra base de datos.

    def getCollection(self, collectionName):

        if collectionName == 'Companies':
            return self.db.Companies
        elif collectionName == 'Person':
            return self.db.Person
        elif collectionName == 'Location':
            return self.db.Location
        else:
            return None


