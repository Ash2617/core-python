#creating a thread without making a sub class to Thread class
from threading import *

#create our own class
class MyThread:
    def __init__(self, str):    #constructor that calls Thread class constructor
        self.str = str

    def display(self, x, y):
        print(self.str)
        print("The args are: ", x, y)

#create an instance to our class and store 'Hello' string
obj = MyThread("Hello")

#create a thread to run display method of obj
t1 = Thread(target=obj.display, args=(1,2))

#run the thread
t1.start()