#A class with a method
class Myclass:
    def calculate(self, x):
        print("Square value = ", x*x)

#all objects share same calculate() method
obj1 = Myclass()
obj1.calculate(2)

obj2 = Myclass()
obj2.calculate(3)

obj3 = Myclass()
obj3.calculate(4)