
class book:

    def __init__(self, bookId, title, description, author):
        self._bookId = bookId
        self._title = title
        self._description = description
        self._author = author
        self._rented = False

    def getbookId(self):
        return self._bookId
    def gettitle(self):
        return self._title
    def getauthor(self):
        return self._author
    def getdescription(self):
        return self._description
    def setbookId(self, newid):
        self._bookId = newid
    def settitle(self, newtitle):
        self._title = newtitle
    def setdescription(self, new):
        self._description = new
    def setauthor(self, author):
        self._author = author
    
    def setRented(self):
        book.rented = True
    def checkRented(self):
        return self._rented
    
    def updateBook (self, newTitle, newDescription, newAuthor):
        if newTitle and (not newTitle.isspace()):
            self.settitle(newTitle)
        if newDescription and (not newDescription.isspace()):
            self.setdescription(newDescription)  
        if newAuthor and (not newAuthor.isspace()):
            self.setauthor(newAuthor)
 
    def __str__(self):
        return "Book ID: " + self._bookId + ", Title: " + self._title + ", Description: " + self._description + ", Author: " + self._author + ";"
'''
newstr = '\n'
if newstr.isspace() == False:
    print("not empty")

else: 
    print("empty")
                    '''