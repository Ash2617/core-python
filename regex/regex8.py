#retrieve words starting with a numeric digit
import re
str = "The meeting will be conducted on 1st and 21st of every month"
result = re.findall(r"\d[\w]*", str)
for word in result:
    print(word)

#all words having 5 characters
str1 = "one two three four five six seven 8 9 10"
res = re.findall(r"\b\w{5}\b", str1)
print(res)

#all words having 5 characters using search
str2 = "one two three four five six seven 8 9 10"
res1 = re.search(r"\b\w{5}\b", str2)
print(res1.group())

#all words having atleast 4 characters
str1 = "one two three four five six seven 8 9 10"
res = re.findall(r"\b\w{4,}\b", str1)
print(res)

#all words having 3 or 4 or 5 characters
str1 = "one two three four five six seven 8 9 10"
res = re.findall(r"\b\w{3,5}\b", str1)
print(res)

#all words having only single digits
str1 = "one two three four five six seven 8 9 10"
res = re.findall(r"\b\d\b", str1)
print(res)