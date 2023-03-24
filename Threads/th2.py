#creating a thread without using a class
from threading import *
#create a function
def display():
    print("Hello i'm running")

#create a thread and run the function for 5 times
for _ in range(5):
    t = Thread(target=display)  #create a thread and specify the function as its target
    #run the thread
    t.start()