#finding the day of the year
from datetime import *
#get today's date
td = date.today()
print(td)

#%j returns day of the year as : 001, 002....366
s1 = td.strftime("%j")
print("today is", s1, "th day of the year")

#find the week day name
s2 = td.strftime("%A")
print("It is ", s2)