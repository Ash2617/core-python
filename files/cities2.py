#reading city name based on record number
#take the record size as 20 bytes
reclen = 20

#open the file in binary mode for reading
with open("cities.bin", "rb") as f:
    n = int(input("Enter record number: "))
    #move file pointer to the n-1 th record
    f.seek(reclen*(n-1))
    #get the nth record with characters
    str = f.read(reclen)
    #convert the byte string into ordinary string
    print(str.decode())