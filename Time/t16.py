#displaying a range of continuous dates
from datetime import *

#start with today
d = date.today()
print(d)

#add 1 to 9 days and get future dates
for x in range(1, 10):
    nextdate = d + timedelta(days=x)
    print(nextdate)