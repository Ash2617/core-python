# a linked list that stores a group of strings
#create an empty linked list
ll = []

#add some string type elements to ll
ll.append("India")
ll.append("Japan")
ll.append("America")

#display the list
print("The existing list is : ", ll)

#display menu
choice = 0
while choice<5:
    print("LINKED LIST OPERATIONS")
    print("1 Add element")
    print("2 Remove element")
    print("3 Replace element")
    print("4 Search for element")
    print("5 Exit")
    choice = int(input("Enter your choice: "))

    #perform a task depending on user choice
    if choice==1:
        element = input("Enter element: ")
        pos = int(input("At what position? "))
        ll.insert(pos, element)

    elif choice==2:
        try:
            element = input("Enter element: ")
            ll.remove(element)
        except ValueError:
            print("Element not found")
    
    elif choice==3:
        element = input("Enter new element: ")
        pos = int(input("At what position? "))
        ll.pop(pos)
        ll.insert(pos, element)

    elif choice==4:
        element = input("Enter element: ")
        try:
            pos = ll.index(element)
            print("Element found at position: ", pos)
        except ValueError:
            print("Element not found")

    else:
        break

    #display the list elements
    print("List = ", ll)