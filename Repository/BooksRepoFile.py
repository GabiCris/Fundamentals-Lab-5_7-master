
from Repository.BooksRepo import bookList
from classes.books import book

class BooksRepoFile(bookList):

    def __init__(self, filename = "books.txt"):
        bookList.__init__(self)
        self._fileName = filename
        self.loadFromFile()
    
    def addBook(self, book):
        bookList.addBook(self, book)
        self.storeToFile()
    
    def removeBook(self, bookId):
        bookList.removeBook(self, bookId)
        self.storeToFile()
    
    def updateBook(self, bookId, args):
        bookList.updateBook(self, bookId, args)
        self.storeToFile()

    def loadFromFile(self):
        try:
            f = open(self._fileName, "r")
            line = f.readline().strip()
            while line != "":
                attrs = line.split(" ")
                book1 = book(attrs[0], attrs[1], attrs[2], attrs[3])
                bookList.addBook(self, book1)
                line = f.readline().strip()
        except:
            raise Exception("Could not load from File!")
        finally:
            f.close()
    
    def storeToFile(self):
        f = open(self._fileName, "w")
        sts = bookList.getAll(self)
        for book in sts:
            strf = book._bookId + " " + book._title + " " + book._description + " " + book._author + "\n"
            f.write(strf)
        f.close()