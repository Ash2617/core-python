#copying an image into a file
#open the files in binary mode
f1 = open("king.jpg", "rb")
f2 = open("raja.jpg", "wb")

#read bytes from f1 and write into f2
bytes = f1.read()
f2.write(bytes)

#close the files
f1.close()
f2.close()