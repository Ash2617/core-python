import re
str = "Kumbhmela will be conducted at Allahabad in India"
res = re.sub(r"Allahabad", "Prayagraj", str)
print(res)

str1 = "a doctor a day keeps the apple away"
result = re.findall(r"a[\w]*", str1)

#findall() returns a list. Retrieve the elements from the list
for word in result:
    print(word)

print("--------")


""" or alternatively"""

result = re.findall(r"\ba[\w]*\b", str1)

#findall() returns a list. Retrieve the elements from the list
for word in result:
    print(word)