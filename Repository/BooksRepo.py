from classes.books import book

class bookList:
    def __init__(self):
        self._bookList = []
    
    @staticmethod
    def _verifyId (l, bookId):
        for entry in l:
            if entry.getbookId() == bookId:
                raise ValueError("There is already a book entry with that id.")

    def addBook(self, book):
        bookList._verifyId(self._bookList, book.getbookId())
        self._bookList.append(book)
        
    def removeBook (self, bookId):
        for book in self._bookList:
            if book._bookId == bookId:
                self._bookList.remove(book)
                break
    
    def findBook (self, searchId):
        for book in self._bookList:
            if book.getbookId() == searchId:
                #return self._bookList.index(book)
                return book
        raise Exception("There is no book with the specified ID!")
    
    def findBookByTitle(self, title):
        l = []
        for book in self._bookList:
            if title.lower() in book.gettitle().lower():
                l.append(book)
        return l
    def findBookByDesc(self, desc):
        l = []
        for book in self._bookList:
            if desc.lower() in book.getdescription().lower():
                l.append(book)
        return l
    def findBookByAuthor(self, auth):
        l = []
        for book in self._bookList:
            if auth.lower() in book.getauthor().lower():
                l.append(book)
        return l
    
    def __str__(self):
        string = ''
        for book in self._bookList:
            string += str(book)
            string += '\n'
        return string
    
        
        
        
class bookListExceptions(Exception):
    def __init__(self, message):
        self._message = message
    
    def __str__(self):
        return self._message
'''
l = bookList()
bok = book("100","HP","Best","JkR")
bok2 = book("12", "lawl", "as", "eu0")
bok3 = book("10", "Viatz", "as", "andrei")
bok.updateBook("15", "eu", "sunt", "boss")
l.addBook(bok)
l.addBook(bok2)
l.addBook(bok3)
'''