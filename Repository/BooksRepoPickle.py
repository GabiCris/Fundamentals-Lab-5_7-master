
from Repository.BooksRepo import bookList
import pickle

class BooksRepoFilePickle(bookList):

    def __init__(self, filename = "books.pickle"):
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
        f = open(self._fileName, "rb")
        
        try:
            self._data = pickle.load(f)
        except EOFError:
            self._data = []
        except Exception as e:
            raise e
        finally:
            f.close()
    
    def storeToFile(self):
        f = open(self._fileName, "wb")
        pickle.dump(self._data, f)
        f.close()