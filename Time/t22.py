#to display calendar of given month of the year
from calendar import *
#ask for month and year
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

#display the calendar for that month
str = month(yy,mm)
print(str)