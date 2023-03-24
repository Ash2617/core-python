#creating a file with strings
#open the file for writing data
f = open("myfile.txt", "w")

#enter strings from keyboard
print("Enter text (@ at end): ")
while str != "@":
    str = input()   #accept string in str
    #write the string into file
    if(str!="@"):
        f.write(str+"\n")

#closing the file
f.close()