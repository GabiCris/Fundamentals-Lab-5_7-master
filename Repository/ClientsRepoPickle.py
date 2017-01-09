from Repository.ClientsRepo import clients
import pickle

class ClientsRepoFilePicke(clients):

    def __init__(self, filename = "clients.pickle"):
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
        f = open(self._fileName, "rb")
        
        try:
            self._data = pickle.load(f)
        except EOFError:
            self._data = []
        except Exception as e:
            raise e
        finally:
            f.close()
    
    def storeToFile(self):
        f = open(self._fileName, "wb")
        pickle.dump(self._data, f)
        f.close()