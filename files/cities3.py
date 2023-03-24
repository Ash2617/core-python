#searching the city name in the file
import os

#take the record size as 20 characters
reclen = 20

#find size of the file
size = os.path.getsize("cities.bin")
print("Size of the file = {} bytes".format(size))

#find number of records in the file
n = int(size/reclen)
print("No. of records = {}".format(n))

#open the file in binary mode for reading
with open("cities.bin", "rb") as f:
    name = input("Enter city name: ")
    #convert name into binary string
    name = name.encode()
    #position represents the position of file pointer
    position = 0

    #found becomes True if city is found in the file
    found = False

    #repeat for n records in the file
    for i in range(n):
        #place the file pointer at position
        f.seek(position)
        #read 20 characters
        str = f.read(20)
        #if found
        if name in str:
            print("Found at record no: ", i+1)
            found = True
        #go to the next record
        position+=reclen

    if not found:
        print("City not found")