#single task using a single thread
from threading import *
from time import *

#create our own class
class MyThread:
    def prepareTea(self):   #a method that preforms 3 tasks one by one
        self.task1()
        self.task2()
        self.task3()

    def task1(self):
        print("Boil milk and tea powder for 5 mins...", end="")
        sleep(5)
        print("Done")

    def task2(self):
        print("Add sugar and boil for 3 mins...", end="")
        sleep(3)
        print("Done")

    def task3(self):
        print("Filter it and serve...", end="")
        print("Done")

#create an instance to our class
obj = MyThread()

#create a thread and run prepareTea method of obj
t = Thread(target=obj.prepareTea)
t.start()