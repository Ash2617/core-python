import re
str = "Hello World"
if res := re.search(r"^He", str):
    print("String starts with 'He'")
else:
    print("String does not start with 'He'")

print("-----------")

str = "Hello World"
if res := re.search(r"World$", str):
    print("String ends with 'World'")
else:
    print("String does not end with 'World'")

print("-----------")

str = "Hello World"
if res := re.search(r"world$", str):
    print("String ends with 'world'")
else:
    print("String does not end with 'world'")

print("-----------")

str = "Hello World"
if res := re.search(r"world$", str, re.IGNORECASE):
    print("String ends with 'world'")
else:
    print("String does not end with 'world'")