#creating a thread without using a class
from threading import *

#create a function
def display(str):
    print(str)
#create a thread and run the function for 5 times
for _ in range(5):
    t = Thread(target=display, args=("Hello", ))  #create a thread and specify the function as its target
    t.start()