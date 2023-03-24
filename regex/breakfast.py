import re
import urllib.request

#open the html file using urlopen() method
f = urllib.request.urlopen(r"file:///f|regex\breakfast.html")

#read data from the file object to the text string
text = f.read()

#convert the byte string into a normal string
str = text.decode()

#apply regular expression on the string
result = re.findall(r"<td>\w+</td>\s<td>(\w+)</td>\s<td>(\d{1,}.\d{1,})</td>", str)

#display result
print(result)
#display the items of the result
for item, price in result:
    print("Item=%-15s Price=%-10s" %(item, price))

f.close()