#reading characters from file
#open the file for reading data
f = open("myfile.txt", "r")

#read all characters from file 
str = f.read()

#display them on screen
print(str)

#closing the file
f.close()