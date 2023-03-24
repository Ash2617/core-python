#checking if file exists and then reading data
import os, sys

#open the file for reading data
fname = input("Enter filename: ")

if os.path.isfile(fname):
    f = open(fname, "r")
else:
    print(fname+" does not exist")
    sys.exit()

#read strings from the file
print("The file contents are: ")
str = f.read()
print(str)

f.close()