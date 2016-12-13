from Ctrl.RentalsController import RentalsController
from Ctrl.UndoController import FunctionCall, Operation


class RentalsControllerUndo(RentalsController):
    def __init__(self, undoController, repo, booksRepo, clientsRepo):
        RentalsController.__init__(self, repo, booksRepo, clientsRepo)
        self._undoController = undoController
        
    def rental_ctrl_add(self, rental):
        RentalsController.rental_ctrl_add(self, rental)
        
        undo = FunctionCall(self.rental_ctrl_remove, rental)
        redo = FunctionCall(self.rental_ctrl_add, rental)
        
        self._undoController.add_operationList([Operation(undo, redo)])
        
    def rental_ctrl_remove(self, rental):
        RentalsController.rental_ctrl_remove(self, rental)
        
        undo = FunctionCall(self.rental_ctrl_add, rental)
        redo = FunctionCall(self.rental_ctrl_remove, rental)
        self._undoController.add_operationList([Operation(undo, redo)])