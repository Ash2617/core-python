#deleting a record from the file
import os

#take the record size as 20 characters
reclen = 20

#find size of the file
size = os.path.getsize("cities.bin")

#find number of records in the file
n = int(size/reclen)

#open the cities.bin for reading
f1 = open("cities.bin", "rb")

#open ncities.bin for writing
f2 = open("ncities.bin", "wb")

#accept city name from the keyboard
city = input("Enter city name to delete: ")

#add spaces to make its length to be 20
ln = len(city)
city = city + (reclen-ln)*" "

#convert city name into binary string
city = city.encode()

#repeat for n records in the file
for i in range(n):
    #read one record from f1 file
    str = f1.read(reclen)
    #if it is not the city name, store into ncities file
    if(str != city):
        f2.write(str)

print("Record deleted")

#close the files
f1.close()
f2.close()

#delete the cities.bin file
os.remove("cities.bin")

#rename ncities.bin as cities.bin
os.rename("ncities.bin", "cities.bin")