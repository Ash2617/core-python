#to view contents of zipped files
from zipfile import *

#Open zip file
z = ZipFile('test.zip','r')

#extract all the file names which are in the zip file
z.extractall()