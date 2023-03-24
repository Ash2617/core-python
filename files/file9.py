#with statement to open a file
with open("sample.txt", "w") as f:
    f.write("I am a learner\n")
    f.write("Python is attractive\n")

#10 using with statement to open a file
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())     #to strip addl space due to \n