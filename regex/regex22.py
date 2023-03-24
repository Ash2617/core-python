#displaying marks and names
import re
str = "Rahul got 78 marks, Ajay got 88 marks whereas Utkarsh got 101 marks"

#extract marks 
marks = re.findall(r"\d{2,3}", str)
print(marks)
#extract names. Hint: start with capitals
names = re.findall(r"[A-Z]\w+", str)
print(names)

print("----------")

str = "Meeting may be at 8am or 9am or 4pm or 5pm"
#extract timings
res = re.findall(r"\dam|\dpm", str)
print(res)