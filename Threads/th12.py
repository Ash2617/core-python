#solution for dead lock of threads
from threading import *

#take 2 locks
l1 = Lock()
l2 = Lock()

#create a function for booking a ticket
def bookticket():
    l1.acquire()
    print("Bookticket locked train")
    print("Bookticket wants to lock on compartment")
    l2.acquire()
    print("Bookticket locked compartment")
    l2.release()
    l1.release()
    print("Booking ticket done")

#create a function for cancelling a ticket
def cancelticket():
    l1.acquire()
    print("Cancelticket locked compartment")
    print("Cancelticket wants to lock on train")
    l2.acquire()
    print("Cancelticket locked train")
    l2.release()
    l1.release()
    print("Cancelling ticket done")

#create 2 threads and run them
t1 = Thread(target=bookticket)
t2 = Thread(target=cancelticket)

t1.start()
t2.start()