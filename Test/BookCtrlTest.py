
import unittest
from Ctrl.BooksController import BooksController
from classes.books import book
from Repository.BooksRepo import bookList


class BookCtrlTest(unittest.TestCase):

    def setUp(self):
        repo = bookList()
        self._ctrl = BooksController(repo)
        

    def testCtrl(self):
        self.assertEqual(len(self._ctrl._Books_repo._bookList), 0)
        book1 = book("2","HitchHiker","Voted","Douglas Adams")
        self._ctrl.book_ctrl_add(book1)
        self.assertEqual(len(self._ctrl._Books_repo._bookList), 1)
        
    def testAdd(self):
        book1 = book("3","HitchHiker","Voted","Douglas Adams")
        self._ctrl.book_ctrl_add(book1)
        self.assertRaises(ValueError, self._ctrl.book_ctrl_add,book("3","HitchHiker","Voted","Douglas Adams"))
        self._ctrl.book_ctrl_add(book("2","HitchHiker","Voted","Douglas Adams"))
        self.assertEqual(len(self._ctrl._Books_repo._bookList), 2)
        
    def testRemove(self):
        self._ctrl.book_ctrl_add(book("1","HP","Best","JkR"))
        self._ctrl.book_ctrl_add(book("2","HitchHiker","Voted","Douglas Adams"))
        self._ctrl.book_ctrl_add(book("3", "py", "as", "andrei"))
        self._ctrl.book_ctrl_add(book("4", "Anna", "drama", "T"))
        self._ctrl.book_ctrl_add(book("5","Pride and Prejudice","Russian","D"))
        
        self.assertEqual(len(self._ctrl._Books_repo._bookList), 5)
        self._ctrl.book_ctrl_remove('2')
        self._ctrl.book_ctrl_remove('3')
        self.assertEqual(len(self._ctrl._Books_repo._bookList), 3)
        
        self.assertRaises(Exception, self._ctrl.book_ctrl_remove, '2')
        self.assertRaises(Exception, self._ctrl.book_ctrl_remove, '7')
    
    def testUpdate(self):
        self._ctrl.book_ctrl_add(book("1","HP","Best","JkR"))
        self._ctrl.book_ctrl_add(book("2","HitchHiker","Voted","Douglas Adams"))
        
        self._ctrl.book_ctrl_update("1", ["Harry", "JKK", "J"])
        self.assertEqual(self._ctrl.book_SearchById("1").gettitle(), "Harry")
        self.assertEqual(self._ctrl.book_SearchById("1").getauthor(), "J")
        self._ctrl.book_ctrl_update("2", ["", "j", ""])
        self.assertEqual(self._ctrl.book_SearchById("2").getauthor(), "Douglas Adams")
        
        self.assertRaises(Exception, self._ctrl.book_ctrl_update,"7", [])
        
    def testSearch(self):
        self._ctrl.book_ctrl_add(book("1","HP","Best","JkR"))
        self._ctrl.book_ctrl_add(book("2","HitchHiker","Voted","Douglas Adams"))
        
        self.assertEqual(self._ctrl.book_SearchByAuthor("Jkr")[0].getbookId(), "1")
        self.assertRaises(Exception, self._ctrl.book_SearchByAuthor,"7asa")
        self.assertRaises(Exception, self._ctrl.book_SearchByDescription,"7aa234sa")
        self.assertRaises(Exception, self._ctrl.book_SearchByTitle,"7aa234sa")
        
    def testFind(self):
        self._ctrl.book_ctrl_add(book("1","HP","Best","JkR"))
        self._ctrl.book_ctrl_add(book("2","HitchHiker","Voted","Douglas Adams"))
        
        self.assertEqual(self._ctrl.book_isBookId("1"), True)
        self.assertEqual(self._ctrl.book_isBookId("2"), True)
        
        self.assertRaises(Exception, self._ctrl.book_isBookId,"5")
        self.assertRaises(Exception, self._ctrl.book_isBookId,"ad")
    
    def testSearchAuthor(self):
        self._ctrl.book_ctrl_add(book("1","HP","Best","JkR"))
        self._ctrl.book_ctrl_add(book("2","HitchHiker","Voted","Douglas Adams"))
        
        self.assertEqual(self._ctrl.book_SearchByAuthor("Jkr")[0].getbookId(), "1")
        self.assertRaises(Exception, self._ctrl.book_SearchByAuthor,"7asa")
        
    def testSearchDescription(self):
        self._ctrl.book_ctrl_add(book("1","HP","Best","JkR"))
        self._ctrl.book_ctrl_add(book("2","HitchHiker","Voted","Douglas Adams"))
        
        self.assertRaises(Exception, self._ctrl.book_SearchByDescription,"7aa234sa")
        
    def testSearchTitle(self):
        self._ctrl.book_ctrl_add(book("6","Don Quixote","Classic","Cervantes"))
        self._ctrl.book_ctrl_add(book("9","The great Gatsby","Movie","Fitzgerald"))
        
        self.assertRaises(Exception, self._ctrl.book_SearchByTitle,"zzz")
        self.assertRaises(Exception, self._ctrl.book_SearchByTitle,"7aa234sa")