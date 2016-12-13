from classes.books import book
from _datetime import datetime
from classes.clients import client
from classes.rental import rental
from builtins import AssertionError

# TODO: add specifications and tests

class ui:     
    def __init__(self, b, c, r):
        self._books = b
        self._clients = c
        self._rentals = r
    
    @staticmethod
    def printMenu():
        string = '\nAvailable commands:\n'
        string += '\t 1 - Add book or client\n'
        string += '\t 2 - Remove book or client\n'
        string += '\t 3 - Update book or client information\n'
        string += '\t 4 - List book list, client list or rental list\n'
        string += '\t 5 - Rent book\n'
        string += '\t 6 - Return book\n'
        string += '\t 7 - Search Books\n'
        string += '\t 8 - Search Clients\n'
        string += '\t 9 - Show Statistics\n'
        string += '\t 0 - Exit\n'
        print(string)
    
    def menu(self):
        alive = True
        command_list = {'1':ui.f_add,
                        '2':ui.f_remove,
                        '3':ui.f_update,
                        '4':ui.f_print,
                        '5':ui.f_rent,
                        '6':ui.f_return,
                        '7':ui.search_books,
                        '8':ui.search_clients,
                        '9':ui.statistics_call}
        while alive:
            ui.printMenu()
            try:
                cmd = ui.get_command()
                if cmd == '0':
                    print("Thanks for using!")
                    alive = False
                else:
                    command_list[cmd](self)
            except Exception as ex:
                print (ex)
    
    @staticmethod
    def get_command():
        try:
            cmd = int(input("Please input command: "))
            assert cmd in range (0,10)
        except AssertionError:
            raise Exception("There is no command with the specified number.")
        except:
            raise Exception("Please input an integer with value between 0 and 7!")
        else:
            return str(cmd)
            
    @staticmethod
    def print_add_choices():
        msg = ''
        msg +='\t\t 1. Add a book entry.\n'
        msg +='\t\t 2. Add a new client.'
        return (msg)
    @staticmethod
    def read_add_remove_cmd():
        try:
            cmd = int(input("Please input command: "))
            assert cmd in range (1, 4)
        except:
            raise Exception("Please input 1 or 2")
        else:
            cmd = str(cmd)
            return cmd
    
    @staticmethod
    def get_book():
        try:
            bookId = input("Book Id: ")
            title = input("Book Title: ")
            description = input("Description: ")
            author = input("Author: ")
        except:
            print ("Invalid data.")
        return book(bookId, title, description, author)

    @staticmethod
    def get_client():
        try:
            name = input("Client name: ")
        except:
            raise Exception("Invalid Data")
        return name
    
    def f_add(self, *args):
        print(ui.print_add_choices())
        cmd = ui.read_add_remove_cmd()
        if cmd == '1':
            try:
                self._books.book_ctrl_add(ui.get_book())
            except Exception as e:
                print (e)
        if cmd == '2':
            try:
                self._clients.client_ctrl_add(ui.get_client())
            except Exception as e:
                print(e)
    
    @staticmethod
    def print_remove_choices():
        msg = ''
        msg +='\t\t 1. Remove a book entry by ID.\n'
        msg +='\t\t 2. Remove a client by ID.'
        return (msg)
    
    @staticmethod
    def get_id():
        try:
            idx = int(input("ID: "))
        except:
            print ("Please input an integer!")
        else:
            idx = str(idx)
            return idx
    
    def f_remove (self, *args):
        print (ui.print_remove_choices())
        cmd = ui.read_add_remove_cmd()
        if cmd == '1':
            bookId = ui.get_id()
            self._books.book_ctrl_remove(bookId)
            self._rentals.rental_ctrl_removeByBookId(bookId)
        if cmd == '2':
            self._clients.client_ctrl_remove(ui.get_id())
    
    @staticmethod
    def print_update_choices():
        msg = ''
        msg +='\t\t 1. Update a book entry by ID.\n'
        msg +='\t\t 2. Update a client by ID.'
        return (msg)
    
    @staticmethod
    def get_book_args():
        try:
            title = input("New Title: ")
            description = input("New Description: ")
            author = input("New Author: ")
        except:
            print ("Invalid data.")
        return (title, description, author)
            
    def f_update(self, *args):
        print(ui.print_update_choices())
        cmd = ui.read_add_remove_cmd()
        if cmd == '1':
            searchId = ui.get_id()
            args = ui.get_book_args()
            try:
                self._books.book_ctrl_update(searchId, args)
            except Exception as x:
                print(x)
        elif cmd == '2':
            searchId = ui.get_id()
            clientName = ui.get_client()
            try:
                self._clients.client_ctrl_update(searchId, client(searchId, clientName))
            except Exception as x:
                print(x)
                
    @staticmethod
    def print_choices():
        msg = ''
        msg +='\t\t 1. Print all books.\n'
        msg +='\t\t 2. Print all clients.\n'
        msg +='\t\t 3. Print all rentals.'
        return (msg)
        
    def f_print (self, *args):
        print(ui.print_choices())
        cmd = ui.read_add_remove_cmd()
        if cmd == '1':
            print(self._books)
        if cmd == '2':
            print(self._clients)
        if cmd == '3':
            print(self._rentals)
    @staticmethod
    def get_date():
        userIn = input("(dd/mm/yy): ")    
        d = datetime.strptime(userIn, "%d/%m/%y")
        return d
        #print(d.strftime("%d-%m-%y"))
            
    def get_rental(self):
        try:
            rentId = int(input("Rental ID: "))
            bookId = int(input("Book ID: "))
            #assert self._books.book_isBookId(bookId) == True
            clientId = int(input("Client ID: "))
            #assert self._clients.client_isClientById(clientId) == True
            print("Due Date", end = "")
            dueDate = ui.get_date()
            print("Rented Date", end = "")
            rentedDate = ui.get_date()
        except AssertionError:
            raise Exception("No such book/client!!!")
        except:
            raise Exception("Doh invalid date data!")
        else:
            return rental(str(rentId), str(bookId), str(clientId), dueDate, rentedDate)
        
    def f_rent(self, *args):
        rent = ui.get_rental(self)
        if rent: 
            self._rentals.rental_ctrl_add(rent)
    
    @staticmethod
    def get_return_book ():
        try:
            bookId = int(input("Book ID: "))
            print("Returned Date", end = "")
            rentedDate = ui.get_date()
        except:
            print("Invalid data.")
        else:
            return str(bookId), rentedDate
    def f_return(self, *args):
        argum = ui.get_return_book()
        if argum[0] and argum[1]:
            try:
                self._rentals.rental_ctrl_return(argum[0], argum[1])
            except Exception as x:
                print (x)
    
    @staticmethod
    def print_search_clients():
        msg = ''
        msg +='\t\t 1. Search Clients by ID.\n'
        msg +='\t\t 2. Search Clients by NAME.'
        return msg
    @staticmethod
    def get_field():
        name = input("Search for: ")
        if name:
            return name
        raise Exception("Invalid!!")
    
    '''
    Function to print the elements of a list
    '''
    @staticmethod
    def print_list(l):
        for objct in l:
            print(objct)
        
    def search_clients(self, *args):
        print(ui.print_search_clients())
        cmd = ui.read_add_remove_cmd()
        if cmd == '1':
            searchId = ui.get_id()
            print(self._clients.client_searchById(searchId))
        else:
            searchName = ui.get_field()
            matchingClients = self._clients.client_searchByName(searchName)
            ui.print_list(matchingClients)
            
    @staticmethod
    def get_cmd15():
        try:
            cmd = int(input("Please input command: "))
            assert cmd in range (0,6)
        except:
            raise Exception("Invalid choice!!!")
        return str(cmd)
    
    @staticmethod
    def print_search_books():
        msg = ''
        msg +='\t\t 1. Search Books by ID.\n'
        msg +='\t\t 2. Search Books by TITLE.\n'
        msg +='\t\t 3. Search Books by DESCRIPTION.\n'
        msg +='\t\t 4. Search Books by AUTHOR.'
        return msg
    
    def search_books(self, *args):
        print(ui.print_search_books())
        cmd = ui.get_cmd14()
        if cmd == '1':
            searchId = ui.get_id()
            print(self._books.book_SearchById(searchId))
        if cmd == '2':
            title = ui.get_field()
            l = self._books.book_SearchByTitle(title)
            ui.print_list(l)
        if cmd == '3':
            desc = ui.get_field()
            l = self._books.book_SearchByDescription(desc)
            ui.print_list(l)
        if cmd == '4':
            auth = ui.get_field()
            l = self._books.book_SearchByAuthor(auth)
            ui.print_list(l)
            
    '''    METHODS FOR STATISTICS
    '''

    '''
    Method that prints books in descending order by the times they were rented
    '''
    def f_BooksTimesRented(self):
        result = self._rentals.most_rented_books_times()
        self.print_list(result)
    
    def f_BooksIntervalRented(self):
        result = self._rentals.longest_rented_books_times()
        self.print_list(result)
    
    def f_ClientsMostActive(self):
        result = self._rentals.most_active_clients()
        self.print_list(result)
    
    def f_AuthorMostPopular(self):
        result = self._rentals.most_popular_authors()
        self.print_list(result)   
        
    def f_LateRentals(self):
        result = self._rentals.late_rentals()
        self.print_list(result)
    
    @staticmethod
    def statistics_print():
        msg = ''
        msg +='\t\t 1. MOST rented books by number of times.\n'
        msg +='\t\t 2. MOST rented books by number of days rented.\n'
        msg +='\t\t 3. MOST active clients.\n'
        msg +='\t\t 4. MOST rented author.\n'
        msg +='\t\t 5. Late Rentals.'
        return msg
    
    def statistics_call(self):
        print(ui.statistics_print())
        cmd = ui.get_cmd15()
        if cmd == '1':
            self.f_BooksTimesRented()
        if cmd == '2':
            self.f_BooksIntervalRented()
        if cmd == '3':
            self.f_ClientsMostActive()
        if cmd == '4':
            self.f_AuthorMostPopular()
        if cmd == '5':
            self.f_LateRentals()
            
   
'''      
b1=bookList()
c1=clients()
r1=rentalList()   
a1 = BooksController(b1)
bok = book("100","HP","Best","JkR")
bok2 = book("12", "Anna", "drama", "T")
bok3 = book("10", "py", "as", "andrei")
a1.book_ctrl_add(bok)
a1.book_ctrl_add(bok2)
a1.book_ctrl_add(bok3)

a2 = ClientsController(c1)
cl1 = client("1","Gigel")
cl2 = client("3","Gigo Hagi")
cl3 = client("11","Cris Gabriel")
cl4 = client("7","Gabonte Costel Crisan")
a2.client_ctrl_add(cl1)
a2.client_ctrl_add(cl2)
a2.client_ctrl_add(cl3)
a2.client_ctrl_add(cl4)

a3 = RentalsController(r1)
l = ui(a1,a2,a3)
l.menu()  
print(l._rentals)
'''            