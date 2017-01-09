class clients:
    def __init__(self):
        self._clientList = []
    
    def addClient(self, client):
        clients.verifyClient(self._clientList, client._clientId)
        self._clientList.append(client)
    
    def removeClient(self, clientid):
        self._clientList[:] = [client for client in self._clientList if client._clientId != clientid]
    
    def findClient (self, searchId):
        for client in self._clientList:
            if client._clientId == searchId:
                return client
        raise Exception ("There is no client with that ID!")
    
    def findClientByName(self, namestr):
        matchingClients = []
        for client in self._clientList:
            if namestr.lower() in client.getName().lower():
                matchingClients.append(client)
        return matchingClients
    
    def updateClients(self, clId, cid, name):
        self.findClient(clId).updateClient(cid, name)    
    
    def getAll(self):
        return self._clientList
    
    def __str__(self):
        stri = ''
        for client in self._clientList:
            stri += str(client)
            stri += '\n'
        return stri   
    
    @staticmethod
    def verifyClient(l, aidi):
        for entry in l:
            if entry.getId() == aidi:
                raise ValueError ("There is already a client with that ID!")