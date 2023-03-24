from tkinter import *

#create root window
root = Tk()

#create canvas as a child to root window
c = Canvas(root, bg="black", height=400, width=600)

#copy images into files
file1 = PhotoImage(file="night.gif")
file2 = PhotoImage(file="skull.gif")

#display the image in the canvas in NE direction
#when mouse is placed on night image, we can see skulls
id = c.create_image(550, 50, anchor=NE, image=file1, activeimage=file2)

#display some text below the image
id = c.create_text(300, 40, text="THIS IS THE END", font=("Arial", 20, "bold"), fill="gray")

#add canvas to the root
c.pack()

#wait for any events
root.mainloop()