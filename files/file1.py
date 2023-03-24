#creating a file to store characters
#open the file for writing data
f = open("myfile.txt", "w")

#enter characters from keyboard
str = input("Enter text: ")

#write the string into file
f.write(str)

#closing the file
f.close()