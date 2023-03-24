#difference between two dates along with times
from datetime import *
#create two datetime objects that store date and time
d1 = datetime(2006, 7, 3, 13, 00, 00)
d2 = datetime(2013, 4, 24, 10, 00,00)

#find difference in date and time
diff = d2-d1
print(diff)

#divide days by 7 to get weeks and remaining days
weeks, days = divmod(diff.days, 7)

#divide seconds by 3600 to get hours and remaining seconds
hrs, secs = divmod(diff.seconds, 3600)

#divide remaining seconds with 60 to get minutes
mins = secs//60

#take remaining seconds from remainder of division
secs = secs%60

print("Difference is %d weeks, %d days, %d hours,%d mins, %d secs" %(weeks, days, hrs, mins, secs))