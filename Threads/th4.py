#creating our own thread
from threading import Thread

#create a class as sub class to Thread class
class MyThread(Thread):
    def run(self):  #override the run() method of Thread class
        for i in range(1, 6):
            print(i)

#create an instance of MyThread class
t1 = MyThread()

#start running the thread t1
t1.start()

#wait till thread completes execution
t1.join()