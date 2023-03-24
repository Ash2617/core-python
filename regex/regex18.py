#retrieve date of births from a string
import re
str = "Vijay 20 1-5-2001, Rohit 21 22-10-1990, Sita 22 11-11-2100"
res = re.findall(r"\d{2}-\d{2}-\d{4}", str)
print(res)

print("---------")

str = "Vijay 20 1-5-2001, Rohit 21 22-10-1990, Sita 22 11-11-2100"
res = re.findall(r"\d{1,2}-\d{1,2}-\d{4}", str)
print(res)