#!/usr/bin/env python
FILE = "/home/hk/catkin_ws/src/waypoints/scripts"
RESOLUTION = 0.05
from Tkinter import *
from tkFileDialog import askopenfilename
from PIL import Image, ImageTk

if __name__ == "__main__":
    root = Tk()

    #setting up a tkinter canvas with scrollbars
    frame = Frame(root, bd=2, relief=SUNKEN)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    xscroll = Scrollbar(frame, orient=HORIZONTAL)
    xscroll.grid(row=1, column=0, sticky=E+W)
    yscroll = Scrollbar(frame)
    yscroll.grid(row=0, column=1, sticky=N+S)
    canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    xscroll.config(command=canvas.xview)
    yscroll.config(command=canvas.yview)
    frame.pack(fill=BOTH,expand=1)

    #adding the image
    File = askopenfilename(parent=root, initialdir=FILE,title='Choose an image.')
    img = ImageTk.PhotoImage(Image.open(File))
    canvas.create_image(0,0,image=img,anchor="nw")
    canvas.config(scrollregion=canvas.bbox(ALL))
    
    open("waypointNodes.csv", 'w').close()

    #function to be called when mouse is clicked
    def printcoords(event):
	canvas = event.widget
	x = canvas.canvasx(event.x)
	y = canvas.canvasy(event.y)
	r = 10
	canvas.create_oval(x-r, y-r, x+r, y+r)

	x_transform = (x)*(RESOLUTION) #- 10
	y_transform = 16.5-(y)*(RESOLUTION) 

	f = file("waypointNodes.csv","a")
	f.write(str(x_transform)+","+str(y_transform)+"\n")
	f.close()
	print str(x_transform), str(y_transform)

    canvas.bind("<Button 1>",printcoords)

    root.mainloop()
