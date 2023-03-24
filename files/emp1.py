#pickle - store Emp class objects into emp.dat file
import emp, pickle

#open emp.dat file as a binary file for writing
f = open("emp.dat", "wb")
n = int(input("How many Employees? "))

for _ in range(n):
    id = int(input("Enter ID no. : "))
    name = input("Enter Emp name: ")
    sal = float(input("Enter salary: "))

    #create Emp class object
    e = emp.Emp(id, name, sal)

    #store the object e into file f
    pickle.dump(e, f)

#close the file
f.close()