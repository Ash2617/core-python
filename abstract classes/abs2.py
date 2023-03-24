#abstract class example
from abc import ABC, abstractmethod
class Myclass(ABC):
    @abstractmethod
    def calculate(self, x):
        pass    #empty body no code

#this is sub class of Myclass
class Sub1(Myclass):
    def calculate(self, x):
        print("Square value = ", x*x)
    
#this is another sub class of Myclass
import math
class Sub2(Myclass):
    def calculate(self, x):
        print("Square root = ", math.sqrt(x))

#third sub class of Myclass
class Sub3(Myclass):
    def calculate(self, x):
        print("Cube value = ", x**3)

#create Sub1 class object and call calculate() method
obj1 = Sub1()
obj1.calculate(8)

#create Sub2 class object and call calculate() method
obj1 = Sub2()
obj1.calculate(4096)

#create Sub3 class object and call calculate() method
obj1 = Sub3()
obj1.calculate(4)







#version 2, why is abstract class needed then????
#same functions with lesser lines, find out application of abstract class

class Sub1(object):
    def calculate(self, x):
        print("Square value = ", x*x)
    
#this is another sub class of Myclass
import math
class Sub2(object):
    def calculate(self, x):
        print("Square root = ", math.sqrt(x))

#third sub class of Myclass
class Sub3(object):
    def calculate(self, x):
        print("Cube value = ", x**3)

#create Sub1 class object and call calculate() method
obj1 = Sub1()
obj1.calculate(8)

#create Sub2 class object and call calculate() method
obj1 = Sub2()
obj1.calculate(4096)

#create Sub3 class object and call calculate() method
obj1 = Sub3()
obj1.calculate(4)