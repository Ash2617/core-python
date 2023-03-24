#multitasking using two threads
from threading import *
from time import *

class Theatre:
    #constructor that accepts a string
    def __init__(self, str):
        self.str = str

    #a method that repeats for 5 tickets
    def movieshow(self):
        for i in range(1, 6):
            print(self.str, " : ", i)
            sleep(0.1)

#create two instances to Theatre class
obj1 = Theatre("Cut ticket")
obj2 = Theatre("Show chair")

#create two threads to run movie show()
t1 = Thread(target=obj1.movieshow)
t2 = Thread(target=obj2.movieshow)

#run the threads
t1.start()
t2.start()

#run this several times to find absurd results
#  of Show chair before cutting ticket by Cut ticket