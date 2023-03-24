#using mmap on binary file
import mmap, sys

#display a menu
print("1 to display all the entries")
print("2 to display the phone number")
print("3 to modify phone number")
print("4 exit")
ch = input("Your choice: ")
if ch == "4":
    sys.exit()

with open("phonebook.dat", "r+b") as f:

    #memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)

    #1 to display the entire file
    if(ch == "1"):
        print(mm.read().decode())

    #2 to display phone number
    if(ch == "2"):
        name = input("Enter name: ")
        #find position of name
        n = mm.find(name.encode())
        #go to end of name
        n1 = n+len(name)
        #display the next 10 bytes
        ph = mm[n1: n1+10]
        print("Phone no: ", ph.decode())

    #3 to modify phone number
    if(ch == "3"):
        name = input("Enter name: ")
        #find position of name
        n = mm.find(name.encode())
        #go to end of name
        n1 = n+len(name)
        #enter new phone number
        ph1 = input("Enter new phone number: ")
        #the old phone number is 10 bytes after n1
        mm[n1: n1+10] = ph1.encode()

    #close the map
    mm.close()