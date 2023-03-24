#this is an abstract class. save this as abs3.py
from abc import *
class Car(ABC):
    def __init__(self, regno):
        self.regno = regno

    def openTank(self):
        print("For the car with regno ", self.regno)
        print("Fill the fuel into the tank")

    @abstractmethod
    def steering(self):
        pass

    @abstractmethod
    def braking(self):
        pass