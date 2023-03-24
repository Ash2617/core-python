#thread communication using a queue
from threading import *
from time import *
from queue import *

#create Producer class
class Producer:
    def __init__(self):
        self.q = Queue()

    def produce(self):
        #create 1 to 10 items and add to the Queue
        for i in range(1, 11):
            print("Producing item: ", i)
            self.q.put(i)
            sleep(1)

#create Consumer class
class Consumer:
    def __init__(self, prod):
        self.prod = prod

    def consume(self):
        #recieve 1 to 10 items from the Queue
        for i in range(1, 11):
            print("Receiving item: ", self.prod.q.get(i))

#create producer object
p = Producer()

#create Consumer object and pass Producer object
c = Consumer(p)

#create Producer and Consumer threads
t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()