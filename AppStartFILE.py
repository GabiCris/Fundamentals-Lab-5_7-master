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

booksFile = open("books.txt", 'r+')
clientsFile = open("clients.txt", 'r+')
rentalsFile = open("rentals.txt", 'r+')

for i in range (1,101):
    line = booksFile.readline()
    line = line.split(" ")
    booksRepo.addBook(book(line[0], line[1], line[2], line[3]))

for i in range (1,101):
    line = clientsFile.readline()
    line = line.split(" ")
    clientsRepo.addClient(client(line[0],line[1]))

for i in range(1,101):
    line = rentalsFile.readline()
    line = line.split(" ")
    
    #date 1 3-day-4-5-yr
    #date 2 6-7-8
    date1 = datetime(int(line[5]), int(line[4]), int(line[3]))
    date2 = datetime(int(line[8]), int(line[7]), int(line[6]))
    newRental = rental(line[0], line[1], line[2], date1, date2)
    rentalsRepo.rentBook(newRental)



undoController = UndoController()
rentalsCtrlUndo = RentalsControllerUndo(undoController, rentalsRepo, booksRepo, clientsRepo)
clientsCtrlUndo = ClientsControllerUndo(undoController, rentalsCtrlUndo, clientsRepo)
booksCtrlUndo = BooksControllerUndo(undoController,rentalsCtrlUndo, booksRepo)


UImenu = ui(booksCtrlUndo, clientsCtrlUndo, rentalsCtrlUndo, undoController)
UImenu.menu()

