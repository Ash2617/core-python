#this is a sub class for abstract Car class
from abs3 import Car
class Tesla(Car):
    def steering(self):
        print("Tesla uses intelligent steering")
        print("Ask the car to drive itself")

    def braking(self):
        print("Tesla uses auto brakes")
        print("Ask car to apply brakes and stop it")

#create object to Maruti and use its features
t = Tesla(8055)
t.openTank()
t.steering()
t.braking()