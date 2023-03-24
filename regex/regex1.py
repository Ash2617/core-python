#search for strings starting with m and having total 3 characters
import re

str = "man sun mop run"
if result := re.search(r"m\w\w", str):
    print("1 = ", result.group())

if result := re.findall(r"m\w\w", str):
    print("2 = ", result)

result = re.match(r"m\w\w", str)
print("3 = ", result.group())

str1 = "sun man mop run"

result = re.match(r"m\w\w", str1)
print("4 = ", result)

str2 = "This; is the; 'Core python\'s' book"
result = re.split(r"\W+", str2)
print("5 = ", result)