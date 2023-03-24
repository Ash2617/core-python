#thread communication using Condition object
from threading import *
from time import *

#create Producer class
class Producer:
    def __init__(self):
        self.lst = []
        self.cv = Condition()
        
    def produce(self):
        #lock the condition object
        self.cv.acquire()

        #create 1 to 10 items and add to the list
        for i in range(1, 11):
            self.lst.append(i)
            sleep(1)
            print("Item produced...")
        
        #inform the consumer that production is completed
        self.cv.notify()

        #release the lock
        self.cv.release()

#create Consumer class
class Consumer:
    def __init__(self, prod):
        self.prod = prod

    def consume(self):
        #get lock on condition object
        self.prod.cv.acquire()

        #wait only for 0 seconds after the production
        self.prod.cv.wait(timeout=0)
        
        #release the lock
        self.prod.cv.release()

        #display the content of list 
        print(self.prod.lst)

#create producer object
p = Producer()

#create Consumer object and pass Producer object
c = Consumer(p)

#create Producer and Consumer threads
t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()