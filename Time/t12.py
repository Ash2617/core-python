#finding day of the week
from datetime import *
#accept date month and year from the keyboard
d, m, y = [int(x) for x in input("Enter date (dd/mm/yyyy): ").split("/")]

#store them in dateclass object dt
dt = date(y,m,d)    #always accepts in this sequence y,m,d

#%w - day number and %A full name of the week day
print(dt.strftime("Day %w of the week. This is %A"))