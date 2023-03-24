#unpickle or object de-serialization
import emp, pickle

#open the file to read objects
f = open("emp.dat", "rb")

print("Employee details:  ")
while True:
    try:
        #read object from file f
        obj = pickle.load(f)
        #display the contents of employee object
        obj.display()
    
    except EOFError:
        print("End of file reached.")
        break

f.close()