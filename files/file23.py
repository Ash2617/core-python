import os
#get current working directory
current = os.getcwd()
print("Current directory = ", current)

#create a sub directory by the name mysub
os.mkdir("mysub")

#create a sub-sub directory by the name mysub2
os.mkdir("mysub/mysub2")

#create sub and sub sub directories
os.makedirs("newsub/newsub2")