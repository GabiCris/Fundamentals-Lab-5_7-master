class ClientsController:
    def __init__(self, repo):
        self.__Clients_repo = repo
    
    def client_ctrl_add(self, client):
        self.__Clients_repo.addClient(client)
        
    def client_ctrl_remove(self, clientId):
        self.__Clients_repo.removeClient(clientId)
    
    def client_ctrl_update(self, clientId, newClient):
        self.__Clients_repo.updateClients(clientId, newClient.getId(), newClient.getName())
    
    def client_searchById(self, searchId):
        return self.__Clients_repo.findClient(searchId)
    
    def client_isClientById(self, clientId):
        if self.__Clients_repo.finalize(clientId):
            return True
    
    
    def client_searchByName(self, namestr):
        l = self.__Clients_repo.findClientByName(namestr)
        if l:
            return l
        raise Exception("No Client matching the given name found!!")    
        
    def __str__(self):
        return str(self.__Clients_repo)