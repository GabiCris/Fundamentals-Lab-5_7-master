from classes.books import book
from _datetime import datetime

class RentalsController:
    def __init__(self, repo, booksRepo, clientsRepo):
        self.__Rentals_repo = repo
        self.__Books_repo = booksRepo
        self.__Clients_repo = clientsRepo
        
    def rental_ctrl_add(self, rental):
        self.__Rentals_repo.rentBook(rental)
    
    def rental_ctrl_remove (self, rental):
        self.__Rentals_repo.removeRentalById(rental.get_rentalId())
        
    def rental_ctrl_return(self, bookId, date):
        self.__Rentals_repo.returnBookRentals(bookId).returnBook(date)
    
    def rental_ctrl_removeByBookId(self, bookId):
        self.__Rentals_repo.removeRentalByBookId(bookId)
    
    def rental_ctr_removeByClient(self, client):
        self.__Rentals_repo.removeRentalByClient(client)
        
    
    
    def __str__(self):
        return str(self.__Rentals_repo)
    
    def doNothing(self):
        pass
        
    """    METHODS FOR STATISTICS
    """ 
    
    '''
    Function that takes as input a book and a client object (which can also be NONE) and returns a
    list with only the rentals corresponding to the given input.
    '''
    def filter_rentals (self, book = None, client = None, bookAuthor = None):
        result = []
        for rental in self.__Rentals_repo._rentalList:
            if client != None and rental.get_rentalClientId() != client.getId():
                continue
            if book != None and rental.get_rentalBookId() != book.getbookId():
                continue
            if bookAuthor != None and self.__Books_repo.findBook(rental.get_rentalBookId()).getauthor() != bookAuthor:
                continue
            result.append(rental)
        return result

                
    '''
    method that returns a sorted list with the most rented books by times they were rented
    '''
    def most_rented_books_times (self):
        result = []
        
        for book in self.__Books_repo._bookList:
            rentalsList = self.filter_rentals(book, None)
            if len(rentalsList):
                result.append(BookTimeRented(book, len(rentalsList)))
                
        result.sort(reverse=True)
        return result
    '''
    method that returns a sorted list with the books that were rented for the longest amount of time
    '''
    def longest_rented_books_times(self):
        result = []
        
        for book in self.__Books_repo._bookList:
            rentalsList = self.filter_rentals(book, None)
            interval = 0
            for rental in rentalsList:
                if rental.get_rentalReturnDate != datetime(1,1,1):
                    aux = rental.get_rentalReturnDate() - rental.get_rentalRentedDate()
                    interval += int(aux.days)
            if interval > 0:
                result.append(BookIntervalRented(book, interval))
        
        result.sort(reverse=True)
        return result
    '''
    Method that returns a sorted list of the clients in descending order based on
    the number of days in which the clients had books rented
    '''
    def most_active_clients(self):
        result = []
        
        for client in self.__Clients_repo._clientList:
            rentalsList = self.filter_rentals(None, client)
            days = 0
            for rental in rentalsList:
                if rental.get_rentalReturnDate != datetime(1,1,1):
                    aux = rental.get_rentalReturnDate() - rental.get_rentalRentedDate()
                    days += int(aux.days)
            if days > 0:
                result.append(DaysClient(client, days))
        result.sort(reverse=True)
        return result
    '''
    Method that return a list of the most rented authors in descending order
    '''
    def most_popular_authors(self):
        result = []
        
        for book in self.__Books_repo._bookList:
            rentalsList = self.filter_rentals(None, None, book.getauthor())
            if len(rentalsList):
                result.append(DaysAuthor(book.getauthor(), len(rentalsList)))
        
        result.sort(reverse=True)
        return result
    
    '''
    Method that returns a list of all the books which have been kept past dueDate
    The late rentals list is sorted in descending order of the number of
    days past the Due Date.
    '''
    def late_rentals(self):
        result = []
       
        for book in self.__Books_repo._bookList:
            rentalsList = self.filter_rentals(book, None, None)
            days = 0
            for rental in rentalsList:
                if rental.get_rentalReturnDate() != datetime (1,1,1):
                    interval = datetime.today() - rental.get_rentalDueDate()
                    days = int(interval.days)
            result.append(BookLateRentals(book, days))
        
        result.sort(reverse=True)
        return result
            
            
"""    CLASSES FOR BOOKS RENTAL TIMES STATISTIC
"""
#class for most_rented_books_times method
class BookTimeRented:
    def __init__(self, book, timesRented):
        self.__book = book
        self.__timesRented = timesRented
    
    def get_book(self):
        return self.__book
    def get_timesRented(self):
        return self.__timesRented
    
    def __lt__(self, newobj):
        return self.get_timesRented() < newobj.get_timesRented()
    
    def __str__ (self):
        if self.get_timesRented() != 1:
            return "ID: " + str(self.get_book().getbookId())+", Name: " + str(self.get_book().gettitle()) +" was rented " + str(self.get_timesRented()) +" times;"
        return "ID: " + str(self.get_book().getbookId())+", Name: " + str(self.get_book().gettitle()) +" was rented " + str(self.get_timesRented()) +" time;"
    
#class for longest_rented_books_times method
class BookIntervalRented:
    def __init__(self, book, interval):
        self.__book = book
        self.__interval = interval
    
    def get_book(self):
        return self.__book
    def get_interval(self):
        return self.__interval
    
    def __lt__(self, newobj):
        return self.get_interval() < newobj.get_interval()
    def __str__(self):
        return "ID: " + str(self.get_book().getbookId())+", Name: " + str(self.get_book().gettitle()) +" was rented " + str(self.get_interval()) +" days;"

#class for most_active_clients method
class DaysClient:
    def __init__(self, client, days):
        self.__client = client
        self.__days = days
        
    def get_client(self):
        return self.__client
    def get_days(self):
        return self.__days
    
    def __lt__(self, newobj):
        return self.get_days() < newobj.get_days()
    def __str__(self):
        return "ID " +str(self.get_client().getId()) + ", Client Name: " + str (self.get_client().getName()) + " has rented for " + str(self.get_days()) + " days;"
    
# class for most_popular_author method
class DaysAuthor:
    def __init__(self, author, days):
        self.__author = author
        self.__days = days
        
    def get_author(self):
        return self.__author
    def get_days(self):
        return self.__days
    
    def __lt__(self, newobj):
        return self.get_days() < newobj.get_days()
    def __str__(self):
        if self.get_days() != 1:
            return "Author Name: " + str(self.get_author()) + " has been rented " + str(self.get_days()) + " times;"
        return "Author Name: " + str(self.get_author()) + " has been rented " + str(self.get_days()) + " time;"

# class for late_rentals method
class BookLateRentals:
    def __init__(self, book, interval):
        self.__book = book
        self.__interval = interval
    
    def get_book(self):
        return self.__book
    def get_interval(self):
        return self.__interval
    
    def __lt__(self, newobj):
        return self.get_interval() < newobj.get_interval()
    def __str__(self):
        return "ID: " + str(self.get_book().getbookId())+", Name: " + str(self.get_book().gettitle()) +" is late to be returned by " + str(self.get_interval()) +" days;"
    
    
    
    
    
    
    
    
    