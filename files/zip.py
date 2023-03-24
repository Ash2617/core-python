#zipping the contents of files
from zipfile import *

#create zip file
f = ZipFile("test.zip", "w")

#add some files. these are zipped
f.write("file1.txt")
f.write("file2.txt")
f.write("file3.txt")

#close the zip file
print("test.zip file created....")
f.close()