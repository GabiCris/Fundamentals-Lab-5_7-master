from Ctrl.BooksController import BooksController
from Ctrl.UndoController import FunctionCall, Operation


class BooksControllerUndo(BooksController):
    def __init__(self, undoController, rentalsController, bookRepo):
        BooksController.__init__(self, bookRepo)
        self._undoController = undoController
        self._rentalsController = rentalsController
    
    def book_ctrl_add(self, book):
        BooksController.book_ctrl_add(self, book)
        
        '''Adding operation to undo controller
        '''
        undo = FunctionCall(self.book_ctrl_remove, book.getbookId())
        redo = FunctionCall(self.book_ctrl_add, book)
        operation = Operation(undo, redo)
        
        #adding operation to undoController controller
        operationsList =[]
        operationsList.append(operation)
        self._undoController.add_operationList(operationsList)
        
    def book_ctrl_remove(self, bookId):
        book = BooksController.book_SearchById(self, bookId)
        rentalsList = self._rentalsController.filter_rentals(book)
        
        #remove book entry and rentals of the book
        BooksController.book_ctrl_remove(self, bookId)
        self._rentalsController.rental_ctrl_removeByBookId(bookId)
        
        undo = FunctionCall(self.book_ctrl_add, book)
        redo = FunctionCall(self.book_ctrl_remove, bookId)
        operation = Operation(undo, redo)

        operationsList = []
        operationsList.append(operation)
        for rental in rentalsList:
            undoRental = FunctionCall(self._rentalsController.rental_ctrl_add, rental)
            redoRental = FunctionCall(self._rentalsController.rental_ctrl_remove, rental)
            newOp = Operation(undoRental, redoRental)
            operationsList.append(newOp)
        
        
        self._undoController.add_operationList(operationsList)
        
    def book_ctrl_update(self, bookId, args):
        book = BooksController.book_SearchById(self, bookId)
        originalArgs = [book.gettitle(), book.getdescription(), book.getauthor()]
        BooksController.book_ctrl_update(self, bookId, args)
        
        undo = FunctionCall(self.book_ctrl_update, bookId, originalArgs)
        redo = FunctionCall(self.book_ctrl_update,bookId, args)
        
        operationsList = [Operation(undo,redo)]
        self._undoController.add_operationList(operationsList)
            
            
            
            
