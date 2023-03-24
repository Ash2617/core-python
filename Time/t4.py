#finding current date and time using ctime()
import time
t = time.ctime()    #ctime without epoch time
print(t)
print("---------------")

#finding current date and time
from datetime import *
now = datetime.now()
print(now)
print("Date now: {}/{}/{}".format(now.day, now.month, now.year))
print("Time now: {}:{}:{}".format(now.hour, now.minute, now.second))
print("---------------")

#finding today's date and time
#today() of datetime class gives date and time
dttm = datetime.today()
print("Today's date and time = ", dttm)

dt = date.today()
print("Today's date: ", dt)