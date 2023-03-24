#to test whether leap year or not
from calendar import *
y = int(input("Enter year: "))

if(isleap(y)):
    print(y, "is leap year")
else:
    print(y, "isn't a leap year")