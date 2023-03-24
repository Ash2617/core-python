#thread communication
from threading import *
from time import *

#create Producer class
class Producer:
    def __init__(self):
        self.lst = []
        self.dataprodover = False

    def produce(self):
        #create 1 to 10 items and add to the list
        for i in range(1, 11):
            self.lst.append(i)
            sleep(1)
            print("Item produced...")
        #inform the consumer that the data production is completed
        self.dataprodover=True

#create Consumer class
class Consumer:
    def __init__(self, prod):
        self.prod = prod

    def consume(self):
        #sleep for 100ms as long as dataprodover is False
        while self.prod.dataprodover==False:
            sleep(0.1)
        #display the content of list when data production is over
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