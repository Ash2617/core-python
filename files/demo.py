#create phonebook.dat file
#open the file in wb mode as binary file
with open("phonebook.dat", "wb") as f:
    #write data into the file
    n = int(input("How many entries? "))
    for _ in range(n):
        name = input("Enter name: ")
        phone = input("Enter phone no: ")
        #convert name and phone no. from strings to bytes
        name = name.encode()
        phone = phone.encode()
        #write the data into the file
        f.write(name+phone)