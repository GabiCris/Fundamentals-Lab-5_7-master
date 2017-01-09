from Repository.BooksRepo import bookList
from Repository.ClientsRepo import clients
from Repository.RentalsRepo import rentalList
from menu.ui import ui
from classes.books import book
from classes.clients import client
from classes.rental import rental
from _datetime import datetime
from Ctrl.BooksControllerUNDO import BooksControllerUndo
from Ctrl.UndoController import UndoController
from Ctrl.ClientsControllerUNDO import ClientsControllerUndo
from Ctrl.RentalsControllerUNDO import RentalsControllerUndo

booksRepo = bookList()
clientsRepo = clients()
rentalsRepo = rentalList()

booksRepo.addBook(book("1","HP","Best","JkR"))
booksRepo.addBook(book("2","HitchHiker","Voted","Douglas Adams"))
booksRepo.addBook(book("3", "py", "as", "andrei"))
booksRepo.addBook(book("4", "Anna", "drama", "T"))
booksRepo.addBook(book("5","Pride and Prejudice","Russian","D"))
booksRepo.addBook(book("6","Don Quixote","Classic","Cervantes"))
booksRepo.addBook(book("7","1984","Dystopia","Orwell"))
booksRepo.addBook(book("8","War and Peace","Classic","Tolstoy"))
booksRepo.addBook(book("9","The great Gatsby","Movie","Fitzgerald"))
booksRepo.addBook(book("10","Ulysses","Greek","James Joyce"))

clientsRepo.addClient(client("11", "Lacy Soza"))
clientsRepo.addClient(client("12", "Dorian Sivilis"))
clientsRepo.addClient(client("13", "China Nissen"))
clientsRepo.addClient(client("14", "Jessia Orlando"))
clientsRepo.addClient(client("15", "Fredda Nalls"))
clientsRepo.addClient(client("16", "Rochell Jump"))
clientsRepo.addClient(client("17", "Devon Darville"))

rentalsRepo.rentBook(rental("1", "1", "11",datetime(10,10,10),datetime(11,11,11)))
rentalsRepo._rentalList[0].returnBook(datetime(11,11,11))
rentalsRepo.rentBook(rental("2", "2", "12",datetime(10,10,10),datetime(11,11,11)))
rentalsRepo._rentalList[1].returnBook(datetime(11,11,11))
rentalsRepo.rentBook(rental("3", "3", "11",datetime(11,11,11),datetime(11,12,11)))
rentalsRepo._rentalList[2].returnBook(datetime(15,11,11))
rentalsRepo.rentBook(rental("4", "4", "15",datetime(10,10,10),datetime(11,11,11)))
rentalsRepo._rentalList[3].returnBook(datetime(18,10,10))
rentalsRepo.rentBook(rental("5", "4", "17",datetime(10,10,10),datetime(11,11,11)))
rentalsRepo._rentalList[4].returnBook(datetime(25,11,10))
rentalsRepo.rentBook(rental("6", "5", "11",datetime(10,10,10),datetime(11,11,11)))
rentalsRepo._rentalList[5].returnBook(datetime(13,10,11))
rentalsRepo.rentBook(rental("7", "2", "12",datetime(10,10,10),datetime(11,11,11)))
rentalsRepo._rentalList[6].returnBook(datetime(12,10,10))
rentalsRepo.rentBook(rental("8", "2", "16",datetime(10,10,10),datetime(11,11,11)))

undoController = UndoController()
rentalsCtrlUndo = RentalsControllerUndo(undoController, rentalsRepo, booksRepo, clientsRepo)
clientsCtrlUndo = ClientsControllerUndo(undoController, rentalsCtrlUndo, clientsRepo)
booksCtrlUndo = BooksControllerUndo(undoController,rentalsCtrlUndo, booksRepo)


UImenu = ui(booksCtrlUndo, clientsCtrlUndo, rentalsCtrlUndo, undoController)
#UImenu.menu()
'''
booksCtrlUndo.book_ctrl_add(book("123","War and Peace","Classic","Tolstoy"))
print(booksRepo, '\nBOOK ADD\n')
undoController.undo()
print(undoController._index,'\n',booksRepo)
undoController.redo()
print(undoController._index,'\n',booksRepo)

print(100*'#', '\nBOOK REMOVE\n')
print(rentalsRepo)
booksCtrlUndo.book_ctrl_remove("4")
print(undoController._index,'\n',rentalsRepo, "\n", booksRepo)
undoController.undo()
print(undoController._index,'\n','UNDO REMOVE BOOK \n',rentalsRepo, "\n", booksRepo)
undoController.redo()
print('REDO REMOVE BOOK \n',rentalsRepo, "\n", booksRepo)

print(100*'#', '\nBOOK UPDATE\n')
booksCtrlUndo.book_ctrl_update('1', ['yolo','','yoloswag'])
print(undoController._index,'\n',booksRepo)
undoController.undo()
print(undoController._index,'\n',booksRepo)
undoController.redo()
print(undoController._index,'\n',booksRepo)
'''
'''
print(100*'#', '\nClient ADD\n')
clientsCtrlUndo.client_ctrl_add(client("199", "Gigel Sifilis"))
print("\n", clientsRepo)
undoController.undo()
print("\n", clientsRepo)
undoController.redo()
print("\n", clientsRepo)

print(100*'#', '\nClient REMOVE\n')
print(rentalsRepo)
clientsCtrlUndo.client_ctrl_remove('11')
print("\n", clientsRepo, "\n", rentalsRepo)
undoController.undo()
print("\n", clientsRepo, "\n", rentalsRepo)
undoController.redo()
print("\n", clientsRepo, "\n", rentalsRepo)
'''

'''
UImenu.f_BooksIntervalRented()
print()
UImenu.f_ClientsMostActive()
print()
UImenu.f_AuthorMostPopular()
print()
UImenu.f_LateRentals()
'''