#formatting the current time
from datetime import *
#create date time object with current date time
dt = datetime.now()
print(dt)

#display only time
print("Current time: ", dt.strftime("%H:%M:%S"))