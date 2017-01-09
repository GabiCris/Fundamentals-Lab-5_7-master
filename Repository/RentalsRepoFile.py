from Repository.RentalsRepo import rentalList
from classes.rental import rental
from datetime import datetime

class RentalsRepoFile(rentalList):
    def __init__(self, filename = "rentals.txt"):
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
        try:
            f = open(self._fileName, "r")
            line = f.readline().strip()
            while line != "":
                line = line.split(" ")
                date1 = datetime(int(line[5]), int(line[4]), int(line[3]))
                date2 = datetime(int(line[8]), int(line[7]), int(line[6]))
                newRental = rental(line[0], line[1], line[2], date1, date2)
                rentalList.rentBook(self, newRental)
                line = f.readline().strip()
        except:
            raise Exception("Could not load from File!")
        finally:
            f.close()
    
    def storeToFile(self):
        f = open(self._fileName, "w")
        sts = rentalList.getAll(self)
        for rental in sts:
            strf = rental.get_rentalId() + " " + \
            rental.get_rentalClientId() + " " + rental.get_rentalBookId() + \
            " " + str(rental._rentedDate.day) + \
            " " + str(rental._rentedDate.month)+ " " + \
            str(rental._rentedDate.year)+ " " + \
            str(rental._dueDate.day) + \
            " " + str(rental._dueDate.month)+ \
            " " + str(rental._dueDate.year) + \
            "\n"
            f.write(strf)
        f.close()