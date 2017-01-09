from Repository.ClientsRepo import clients
from classes.clients import client

class ClientsRepoFile(clients):

    def __init__(self, filename = "clients.txt"):
        clients.__init__(self)
        self._fileName = filename
        self.loadFromFile()
        
    def addClient(self, client):
        clients.addClient(self, client)
        self.storeToFile()
    
    def removeClient(self, clientid):
        clients.removeClient(self, clientid)
        self.storeToFile()
    
    def updateClients(self, clId, cid, name):
        clients.updateClients(self, clId, cid, name)
        self.storeToFile()

    def loadFromFile(self):
        try:
            f = open(self._fileName, "r")
            line = f.readline().strip()
            while line != "":
                attrs = line.split(" ")
                client1 = client(attrs[0], attrs[1])
                clients.addClient(self, client1)
                line = f.readline().strip()
        except:
            raise Exception("Could not load from File!")
        finally:
            f.close()
    
    def storeToFile(self):
        f = open(self._fileName, "w")
        sts = clients.getAll(self)
        for client in sts:
            strf = client._clientId + " " + client._name + "\n"
            f.write(strf)
        f.close()