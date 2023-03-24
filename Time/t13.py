#difference of days, weeks and months between two dates
from datetime import *

#enter the two dates from the keyboard
d1, m1, y1 = [int(x) for x in input("Enter first date(dd/mm/yyyy): ").split("/")]
d2, m2, y2 = [int(x) for x in input("Enter second date(dd/mm/yyyy): ").split("/")]

#create date class objects with the input
dt1 = date(y1, m1, d1)
dt2 = date(y2, m2, d2)

#find days difference between these two dates
dt = dt1 - dt2
print("Days difference = ", dt)

#find difference in weeks
weeks, days = divmod(dt.days, 7)
print("Weeks difference = ", weeks)

#find difference in months
months, days = divmod(dt.days, 30)
print("Months difference = ", months)