#every Python program is run by main thread
import threading
print("Let us find the current thread.")

#find the name of present thread
print("Currently running thread: ", threading.current_thread().name)

#check if it is main thread or not
if threading.current_thread()==threading.main_thread():
    print("The current thread is the main thread")
else:
    print("The current thread isn't the main thread")