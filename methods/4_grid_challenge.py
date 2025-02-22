import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")
window.title("Grid Method Tutorial")

l1 = tk.Label(window, text = "Height")
l2 = tk.Label(window, text = "Width")

# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2.grid(row = 1, column = 0, sticky = W, pady = 2)

# entry widgets, used to take entry from user
e1 = Entry(window)
e2 = Entry(window)

# this will arrange entry widgets
e1.grid(row = 0, column = 1, pady = 2)
e2.grid(row = 1, column = 1, pady = 2)

# checkbutton widget
c1 = Checkbutton(window, text = 'Preserve')
c1.grid(row = 2, column = 0, sticky = W, columnspan = 2)

# adding image (remember image should be PNG and not JPG)
img = tk.PhotoImage(file = r'C:\xampp\htdocs\GitHub\itcs103-tkinter-codes\methods\sample.png')
img1 = img.subsample(2, 2)

# setting image with the help of label
Label(window, image = img1).grid(row = 0, column = 2,
       columnspan = 2, rowspan = 2, padx = 5, pady = 5)

# button widget
b1 = tk.Button(window, text = 'Zoom in')
b2 = tk.Button(window, text = 'Zoom out')

# arranging button widgets
b1.grid(row = 2, column = 2, sticky = E)
b2.grid(row = 2, column = 3, sticky = E)

window.mainloop()
