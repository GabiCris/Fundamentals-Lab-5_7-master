from Repository.RentalsRepo import rentalList
import pickle

class RentalsRepoFilePickle(rentalList):
    def __init__(self, filename = "rentals.pickle"):
        rentalList.__init__(self)
        self._fileName = filename
        self.loadFromFile()
    
    def rentBook(self, rental):
        rentalList.rentBook(self, rental)
        self.storeToFile()
        
    def removeRentalById(self, rentalId):
        rentalList.removeRentalById(self, rentalId)
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