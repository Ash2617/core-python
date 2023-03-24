#creating our own thread
from threading import *

#create a class as sub class to Thread class
class MyThread(Thread):
    def __init__(self, str):    #constructor that calls Thread class constructor
        Thread.__init__(self)   #to retain functionality of 'Thread' class
        self.str = str
        
    def run(self):  #override the run() method of Thread class
        print(self.str)

#create an instance of MyThread class
t1 = MyThread("Hello")

#start running the thread t1
t1.start()

#wait till thread completes execution
t1.join()