
import unittest
from Repository.RentalsRepo import rentalList
from Ctrl.RentalsController import RentalsController
from Repository.BooksRepo import bookList

from classes.rental import rental
import datetime
from Ctrl.ClientsController import ClientsController
from Repository.ClientsRepo import clients


class Test(unittest.TestCase):

    def setUp(self):
        repo1 = rentalList()
        bookRepo = bookList()
        clientList = clients()
        
        repo1.rentBook(rental("1", "1", "11",datetime(10,10,10),datetime(11,11,11)))
        
        self._ctrl = RentalsController(repo1, bookRepo, clientList)
        
        
        
    def testAdd(self):
        self.repo.rentBook(rental("5", "4", "17",datetime(10,10,10),datetime(11,11,11)))
        self._ctrl._repo.rentBook(rental("6", "5", "11",datetime(10,10,10),datetime(11,11,11)))
        self._ctrl._repo.rentBook(rental("7", "2", "12",datetime(10,10,10),datetime(11,11,11)))
        self._ctrl._repo.rentBook(rental("8", "2", "16",datetime(10,10,10),datetime(11,11,11)))
        
        self.assertEqual(self._ctrl.__Rentals_repo.rentalsNumber(), 4)
        

