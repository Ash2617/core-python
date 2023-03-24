#retrieve last word of string, if it starts with t
import re
str = "one two three one two thrEE"
result = re.findall(r"t\w*", str)   #\Z matches only at the end of string
print(result)

str = "one two three one two thrEE"
result = re.findall(r"t\w*\Z", str)   #\Z matches only at the end of string
print(result)

str = "one two three one twO"
result = re.findall(r"t\w*\Z", str)   #\Z matches only at the end of string
print(result)

str = "onE two three one"
result = re.findall(r"o\w*\Z", str)   #\Z matches only at the end of string
print(result)