class client:
    def __init__(self, clientId, name):
        self._clientId = clientId
        self._name = name
    
    def getId(self):
        return self._clientId
    def getName(self):
        return self._name
    def setId(self, newId):
        self._clientId = newId
    def setName(self, name):
        self._name = name
    
    def updateClient (self, newId, newName):
        self.setId(newId)
        self.setName(newName)
    
    def __str__(self):
        return "Client ID: " + self._clientId +", Client Name: " + self._name + ";"
