import re

str = "Ashvani Shukla: 9682123458"
res = re.search(r"\d+", str)
print(res.group())

print("---------")

str = "Ashvani Shukla: 9682123458"
res = re.search(r"\D+", str)
print(res.group())

print("---------")

#all words starting with an or ak
str = "anil akhil anant arun arati arundhati abhijit ankur"
res = re.findall(r"a[nk][\w]*", str)
print(res)