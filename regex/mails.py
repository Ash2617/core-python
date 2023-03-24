import re
#open the file for reading
f = open("mails.txt", "r")
str = f.read()
res = re.findall(r'(\w+@\w+)', str)
print(res)

f.close()