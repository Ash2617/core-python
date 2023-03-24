from tkinter import *

#create root window
root = Tk()

#create Canvas as a child to root window
c = Canvas(root, bg="blue", height=700, width=1200, cursor="pencil")

#create a line in the canvas
id = c.create_line(50, 50, 200, 50, 200, 150, width=4, fill="white")

#create an oval in the canvas
id = c.create_oval(100, 100, 400, 300, width=5, fill="yellow", outline="red", activefill="green")

#create a polygon in the canvas
id = c.create_polygon(10, 10, 200, 200, 300, 200, width=3,
                      fill="green", outline="red", smooth=1, activefill="lightblue")

#create a rectangle in the canvas
id = c.create_rectangle(500, 200, 700, 600, width=2, fill="gray", outline="black",
                        activefill="yellow")

#create some text in the canvas
fnt = ("Times", 40, "bold italic underline")
id = c.create_text(500, 100, text="My Canvas", font=fnt, fill="yellow", activefill="green")

#add canvas to the root window
c.pack()

#wait for any events
root.mainloop()