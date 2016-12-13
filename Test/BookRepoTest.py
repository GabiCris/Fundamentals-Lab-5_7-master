
import unittest
from Repository.BooksRepo import bookList
from classes.books import book


class BookRepoTest(unittest.TestCase):

    def setUp(self):
        self._repo = bookList()
        
    def testRepo(self):
        self.assertEqual(len(self._repo._bookList), 0)
        book1 = book("2","HitchHiker","Voted","Douglas Adams")
        self._repo.addBook(book1)
        self.assertEqual(len(self._repo._bookList), 1)
        
        self._repo.findBook(book1.getbookId())
        self.assertEqual(self._repo.removeBook(book1.getbookId()), None)
        self.assertEqual(self._repo.findBookByAuthor(book1.getauthor()), [])
        #self.assertRaises(self._repo.removeBook("11"), book)
        self.assertEqual(len(self._repo._bookList), 0)