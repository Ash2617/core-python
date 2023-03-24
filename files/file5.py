#appending and then reading strings
#open the file for reading data
f = open("myfile.txt", "a+")

#enter strings from keyboard
print("Enter text to append(@ at end): ")
while str != "@":
    str = input()   #accept string in str
    #write the string into file
    if(str != "@"):
        f.write(str+"\n")

#put the file pointer to the beginning of file
f.seek(0,0)

#read strings from the file
print("The file contents are: ")
str = f.read()
print(str)

#closing the file
f.close()