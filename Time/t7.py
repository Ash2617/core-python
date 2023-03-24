#combining date and time
from datetime import *
d = date(1995, 7, 11)
t = time(9, 20)
dt = datetime.combine(d, t)
print(dt)

#create date time objects and change its contents
# from datetime import *
dt1 = datetime(year=2022, month=7, day=18, hour=10, minute=30, second=30)
print(dt1)

#change its year month and hour values
dt2 = dt1.replace(year=2019, day=24, hour=11)
print("changed date = ", dt2)

#formatting the date
td = date.today()
print(td)
#format td and convert into string str
str = td.strftime("%d, %B, %y")
print(str)

str1 = dt.strftime("%d, %B, %y")
print(str1)