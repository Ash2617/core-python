#using stack class of stack.py
from stack import Stack
#create empty stack object
s = Stack()

#display menu
choice = 0
while choice<5:
    print("STACK OPERATIONS")
    print("1 Push element")
    print("2 Pop element")
    print("3 Peep element")
    print("4 Search for element")
    print("5 Exit")
    choice = int(input("Enter your choice: "))

    #perform a task depending on user choice
    if choice==1:
        element = int(input("Enter element: "))
        s.push(element)

    elif choice==2:
        element = s.pop()
        if element == -1:
            print("The stack is empty")
        else:
            print("Popped element = ", element)
    
    elif choice==3:
        element = s.peep()
        print("Top most element = ", element)

    elif choice==4:
        element = int(input("Enter element: "))
        pos = s.search(element)
        if pos == -1:
            print("The stack is empty")
        elif pos == -2:
            print("Element not found in the stack")
        else:
            print("Element found at position: ", pos)
        
    else:
        break

    #display the contents of the stack object
    print("Stack = ", s.display())