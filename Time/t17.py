#to know who is older
from datetime import *

#enter birth dates and store in date class objects
d1, m1, y1 = [int(x) for x in input("Enter first person's DOB(dd/mm/yyy): ").split("/")]
b1 = date(y1, m1, d1)

d2, m2, y2 = [int(x) for x in input("Enter second person's DOB(dd/mm/yyy): ").split("/")]
b2 = date(y2, m2, d2)

#compare the birth dates
if b1==b2:
    print("Both are of same age")
elif b1>b2:
    print("Second person is elder")
else:
    print("First person is elder")