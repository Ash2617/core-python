#using Queue class of que1.py
from que1 import Queue
#create empty queue object
q = Queue()

#display menu
choice = 0
while choice<4:
    print("QUEUE OPERATIONS")
    print("1 Add element")
    print("2 Delete element")
    print("3 Search for element")
    print("4 Exit")
    choice = int(input("Enter your choice: "))

    #perform a task depending on user choice
    if choice==1:
        element = float(input("Enter element: "))
        q.add(element)

    elif choice==2:
        element = q.delete()
        if element == -1:
            print("The queue is empty")
        else:
            print("Deleted element = ", element)

    elif choice==3:
        element = float(input("Enter element: "))
        pos = q.search(element)
        if pos == -1:
            print("The queue is empty")
        elif pos == -2:
            print("Element not found in the queue")
        else:
            print("Element found at position: ", pos)
        
    else:
        break

    #display the contents of the stack object
    print("Queue = ", q.display())