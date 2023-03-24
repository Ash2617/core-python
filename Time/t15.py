#finding future date and time
from datetime import *
#store the date and time in datetime object : d1
d1 = datetime(2023, 3, 22, 9, 15, 00)

#define the duration using timedelta object: period1
period1 = timedelta(days=30, seconds=10, minutes=10, hours=3)

#add the duration to d1 and display
print("The new date and time is: ", d1+period1)