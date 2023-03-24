#converting the epoch time into date and time
import time

#localtime() converts the epoch time into time_struct object t
t = time.localtime(1679376313.5040047)

#retrieve the date from structure t
d = t.tm_mday
m = t.tm_mon
y = t.tm_year
print("Current date is : %d - %d - %d" %(d,m,y))

h = t.tm_hour
m = t.tm_min
s = t.tm_sec
print("Current time is : %d : %d : %d" %(h,m,s))

#convert epoch time into date and time using ctime()
t = time.ctime(1679376313.5040047)
print(t)