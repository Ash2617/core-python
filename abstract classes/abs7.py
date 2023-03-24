#an inerface to send text to any printer
from abc import *
#create an interface
class Printer(ABC):
    @abstractmethod
    def printit(self, text):
        pass
    @abstractmethod
    def disconnect(self):
        pass

#this is a sub class for IBM printer
class IBM(Printer):
    def printit(self, text):
        print(text)
    
    def disconnect(self):
        print("Printing completed on IBM printer")

#this is another sub class for Epson printer
class Epson(Printer):
    def printit(self, text):
        print(text)
    
    def disconnect(self):
        print("Printing complete on Epson printer.")

class UsePrinter:
    #accept printer name as a string from configuration file
    with open("abs7.txt", "r") as f:
        str = f.readline()

    #convert the string into classname
    classname = globals()[str]

    #create an object to that class
    x = classname()

    #call the printit() and disconnect() methods
    x.printit("Hello, this is sent to printer")
    x.disconnect()