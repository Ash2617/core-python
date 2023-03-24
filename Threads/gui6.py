from tkinter import *

#create root window
root = Tk()

#create canvas as child to root window
c = Canvas(root, bg="black", height=300, width=500)

#copy images into files
file1 = PhotoImage(file="king.gif")
file2 = PhotoImage(file="raja.gif")

#display the image in the canvas in NE direction
#when mouse is placed on king image, we can see
id = c.create_image(350, 100, anchor=NE, image=file1, activeimage=file2)

#display some text below the image
id = c.create_text(250, 70, text="THIS IS SPARTAAAA", font=("Arial", 20, "bold"), fill="red")

#add canvas to the root
c.pack()

#wait for any events
root.mainloop()