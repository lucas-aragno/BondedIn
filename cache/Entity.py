import json
class Entity(object):  
    def getSerializable(self):
        return json.dumps(self.__dict__)

    
    
    