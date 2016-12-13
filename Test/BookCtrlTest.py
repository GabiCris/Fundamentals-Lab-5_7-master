
import unittest
from Ctrl.BooksController import BooksController
from classes.books import book
from Repository.BooksRepo import bookList


class BookCtrlTest(unittest.TestCase):

    def setUp(self):
        repo = bookList()
        self._ctrl = BooksController(repo)

    def testCtrl(self):
        self.assertEqual(len(self._ctrl.__Books_repo), 0)
        book1 = book("2","HitchHiker","Voted","Douglas Adams")
        self._ctrl.book_ctrl_add(book1)
        print(self._ctrl.__Books_repo._bookList)
        self.assertEqual(len(self._ctrl.__Books_repo), 1)
