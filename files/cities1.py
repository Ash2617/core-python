#create cities.bin file with cities name
#take the record size as 20 bytes
reclen = 20

#open the file in wb mode as binary file
with open("cities.bin", "wb") as f:
    #write data into the file
    n = int(input("How many entries? "))

    for _ in range(n):
        city = input("Enter city name: ")
        #find the length of city
        ln = len(city)
        #increase the city name to 20 characters
        #by adding remaining spaces
        city = city + (reclen-ln)*" "
        #convert city name into byte string
        city = city.encode()
        #write the city name into the file
        f.write(city)