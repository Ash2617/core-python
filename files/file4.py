#reading strings from a file
#open the file for reading data
f = open("myfile.txt", "r")

#read strings from file
print("The contents of file are: ") 
str = f.read()
print(str)

#closing the file
f.close()