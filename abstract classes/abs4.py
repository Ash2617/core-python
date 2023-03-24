#this is a sub class for abstract Car class
from abs3 import Car
class Maruti(Car):
    def steering(self):
        print("Maruti uses manual steering")
        print("Drive the car")

    def braking(self):
        print("Maruti uses hydraulic brakes")
        print("Apply brakes and stop it")

#create object to Maruti and use its features
m = Maruti(1001)
m.openTank()
m.steering()
m.braking()