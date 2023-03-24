#to measure the time taken by the program
from time import *
#note the starting of the program
t1 = perf_counter()

#do some processing
i, sum = 0, 0
while(i<1000000):
    sum+=i
    i+=1

#make the processor or PVM sleep for 3 seconds
#this is also measured by perf_counter
sleep(3)

#note the ending time of program
t2 = perf_counter()

#find time for the program in seconds
print("Execution time = %f seconds" %(t2-t1))