#creating a daemon thread
from threading import *
from time import *

#to display numbers from 1 to 5 every second
def display():
    for i in range(10):
        print("Normal thread: ", end="")
        print(i+1)
        sleep(1)

#to display date and time once in every 2 seconds
def display_time():
    while True:
        print("Daemon thread: ", end="")
        print(ctime())
        sleep(2)

#create a normal thread and attach it to display() and run it
t = Thread(target=display)
t.start()

#create another thread and attach it to display_time()
d = Thread(target=display_time)

#make the thread daemon
d.daemon = True

#run the daemon thread
d.start()