#multitasking using two threads
from threading import *
from time import *

class Railway:
    #constructor that accepts no. of available berths
    def __init__(self, available):
        self.available = available

    #a method that reserves berths
    def reserve(self, wanted):
        #display no. of available berths
        print("Available no. of berths = ", self.available)

        #if available >= wanted, allot a berth
        if(self.available >= wanted):
            #find the thread name
            name = current_thread().name
            #display berth is alloted for the person
            print("%d berth alloted for %s" %(wanted, name))
            #make time delay so that ticket is printed
            sleep(1.5)
            #decrease the no. of available berths
            self.available-=wanted
        else:
            #if available < wanted, say sorry 
            print("Sorry, no berths to allot")

#create instance to Railway class
#specify only 1 berth is available
obj = Railway(1)

#create 2 threads and specify 1 berth is needed
t1 = Thread(target=obj.reserve, args=(1,))
t2 = Thread(target=obj.reserve, args=(1,))

#give names to the threads
t1.setName("First person")
t2.setName("Second person")

#run the threads
t1.start()
t2.start()