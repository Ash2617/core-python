#to generate random numbers between 100 and 200 every 1.5 secs
import time, random

#generate 10 random numbers
for i in range(10):
    num = random.randrange(100, 200, 5) #generate in range of 100 to 200
    print(num)
    time.sleep(1.5) #suspend execution for 1.5secs