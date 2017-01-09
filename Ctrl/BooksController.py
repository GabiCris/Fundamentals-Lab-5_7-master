class BooksController:
    def __init__(self, repo):
        self._Books_repo = repo
    
    def book_ctrl_add(self, book):
        self._Books_repo.addBook(book)
    
    def book_ctrl_remove(self, bookId):
        self._Books_repo.removeBook(bookId)
    
    '''
    updates the book with the specified bookID with the new args:
    args is a list/touple with 4 elements: 0- id, 1- title, 2- desc, 3- author
    '''
    def book_ctrl_update(self, bookId, args):
        self._Books_repo.updateBook(bookId, args)
        
    def book_SearchById(self, searchId):
        return self._Books_repo.findBook(searchId)
    
    def book_SearchByTitle(self, title):
        matchingBooks = self._Books_repo.findBookByTitle(title)
        if matchingBooks:
            return matchingBooks
        raise Exception("No such books !!!")
    
    def book_SearchByDescription(self, desc):
        matchingBooks = self._Books_repo.findBookByDesc(desc)
        if matchingBooks:
            return matchingBooks
        raise Exception("No such books !!!")
    
    def book_SearchByAuthor(self, auth):
        matchingBooks = self._Books_repo.findBookByAuthor(auth)
        if matchingBooks:
            return matchingBooks
        raise Exception("No such books !!!")
    
    def book_isBookId(self, bookId):
        if self._Books_repo.findBook(bookId):
            return True
    
    def __str__(self):
        return str(self._Books_repo)
        
        