from classes.rental import rental
from _datetime import datetime
from iterStruct.StructureLab9 import iterStruct

class rentalList:
    def __init__(self):
        self._rentalList = iterStruct()
    
    def rentBook (self, rental):
        #TODO VERIFY EXISTANCE OF CLIENT AND BOOK
        self._rentalList.append(rental)
    
    def returnBookRentals(self, bookid):
        for rental in self._rentalList:
            if rental._bookId == bookid:
                return rental
        raise Exception("That book is not rented!")
    
    def removeRentalById(self, rentalId):
        for rental in self._rentalList:
            if rental.get_rentalId() == rentalId:
                self._rentalList.remove(rental)
                
    def removeRentalByBookId(self, bookId):
        '''
        for rental in self._rentalList:
            if rental.get_rentalBookId() == bookId:
                self._rentalList.remove(rental)
        '''
        self._rentalList = [rental for rental in self._rentalList if rental.get_rentalBookId()!= bookId]
    
    def removeRental (self, rental):
        self._rentalList.remove(rental)
        
    def removeRentalByClient(self, client):
        self.rentalList = [rental for rental in self._rentalList if rental.get_rentalClientId()!= client.getId()]
            
    def rentalsNumber(self):
        return len(self._rentalList)
    
    def getAll(self):
        return self._rentalList
    
    def __str__(self):
        msg = ''
        for rental in self._rentalList:
            msg += str(rental)
            msg += '\n'
        return msg

r = rental("1", '2', '3')
r2 = rental('3','4','5')
l = rentalList()

