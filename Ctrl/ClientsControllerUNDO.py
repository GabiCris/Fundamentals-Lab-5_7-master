from Ctrl.ClientsController import ClientsController
from Ctrl.UndoController import FunctionCall, Operation


class ClientsControllerUndo(ClientsController):
    def __init__(self, undoController, rentalsController, clientsRepo):
        ClientsController.__init__(self, clientsRepo)
        self._undoController = undoController
        self._rentalsController = rentalsController
        
    def client_ctrl_add(self, client):
        ClientsController.client_ctrl_add(self, client)
        
        undo = FunctionCall(self.client_ctrl_remove, client.getId())
        redo = FunctionCall(self.client_ctrl_add, client)
        
        self._undoController.add_operationList([Operation(undo,redo)])
        
    def client_ctrl_remove(self, clientId):
        client = ClientsController.client_searchById(self, clientId)
        rentalsList = self._rentalsController.filter_rentals(None, client, None)
        
        ClientsController.client_ctrl_remove(self, clientId)
        for rental in rentalsList:
            self._rentalsController.rental_ctrl_remove(rental)
        
        undo = FunctionCall(self.client_ctrl_add, client)
        redo = FunctionCall(self.client_ctrl_remove, clientId)
        opList =[Operation(undo, redo)]
        
        for rental in rentalsList:
            undoRental = FunctionCall(self._rentalsController.rental_ctrl_add, rental)
            redoRental = FunctionCall(self._rentalsController.rental_ctrl_remove, rental)
            newOp = Operation(undoRental, redoRental)
            opList.append(newOp)
        
        self._undoController.add_operationList(opList)
        
    def client_ctrl_update(self, clientId, newClient):
        oldClient = ClientsController.client_searchById(self, clientId)
        ClientsController.client_ctrl_update(self, clientId, newClient)
        
        undo = FunctionCall(self.client_ctrl_update, clientId, oldClient)
        redo =FunctionCall(self.client_ctrl_update, clientId, newClient)
        self._undoController.add_operationList([Operation(undo,redo)])
        

        