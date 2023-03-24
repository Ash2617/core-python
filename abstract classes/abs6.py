#abstract class works like an inerface
from abc import *
class Myclass(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass

#this is a sub class
class Oracle(Myclass):
    def connect(self):
        print("Connecting to Oracle database...")
    
    def disconnect(self):
        print("Disconnect from Oracle")

#this is another sub class
class Sybase(Myclass):
    def connect(self):
        print("Connecting to Sybase database...")
    
    def disconnect(self):
        print("Disconnect from Sybase")

class Database:
    #accept database name as a string
    str = input("Enter database name: ")

    #convert the string into classname
    classname = globals()[str]

    #create an object to that class
    x = classname()

    #call the connect() and disconnect() methods
    x.connect()
    x.disconnect()