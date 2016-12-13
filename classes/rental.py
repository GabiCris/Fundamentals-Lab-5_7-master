from _datetime import datetime

class rental: 
    def __init__(self, rentalId, bookId, clientId, rentedDate = datetime.today(),dueDate = datetime.today()):
        self._rentalId = rentalId
        self._clientId = clientId
        self._bookId = bookId
        self._rentedDate = rentedDate
        self._dueDate = dueDate
        self._returnDate = datetime(1,1,1)
            
    def get_rentalId(self):
        return self._rentalId
    
    def get_rentalClientId(self):
        return self._clientId
    
    def get_rentalBookId(self):
        return self._bookId
    
    def get_rentalRentedDate (self):
        return self._rentedDate
    
    def get_rentalDueDate(self):
        return self._dueDate
    
    def get_rentalReturnDate(self):
        return self._returnDate
    
    def returnBook (self,returnDate):
        self._returnDate = returnDate
    
    def __str__(self):
        if self._returnDate != datetime(1990, 1, 1):
            return "Rental ID: " + str(self._rentalId) + ", Book Id: " + str(self._bookId)+ ", Client ID: " + str(self._clientId) + ", Rented Date: " + str(self._rentedDate) + ", Due Date: " + str(self._dueDate) + ", Return date: " + str(self._returnDate)#str(self._returnDate.strftime("%d-%m-%y")) + ";"
        else:
            return "Rental ID: " + str(self._rentalId) + ", Book Id: " + str(self._bookId)+ ", Client ID: " + str(self._clientId) + ", Rented Date: " + str(self._rentedDate.strftime("%d-%m-%y")) + ", Due Date: " + str(self._dueDate.strftime("%d-%m-%y")) + ", Return date: Book not yet returned!"
