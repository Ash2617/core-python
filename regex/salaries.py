#retrieve data from a file and write that data into a file
import re
#open the files
f1 = open("salaries.txt", "r")
f2 = open("newfile.txt", "w")

#repeat for each line of the file f1
for line in f1:
    res1 = re.search(r"\d{4}", line)    #extract 4 digit id no.
    res2 = re.search(r"\d{4,}.\d{2}", line) #extract salary
    print(res1.group(), res2.group())
    f2.write(res1.group()+"\t")
    f2.write(res2.group()+"\n")

f1.close()
f2.close()