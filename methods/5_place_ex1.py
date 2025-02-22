import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")
window.title("Place Method Tutorial")

# button widget
b1 = tk.Button(window, text = "Click me !")
b1.place(relx = 1, x =-2, y = 2, anchor = NE)

# label widget
l = tk.Label(window, text = "I'm a Label")
l.place(anchor = NW)
 
# button widget
b2 = tk.Button(window, text = "GFG")
b2.place(relx = 0.5, rely = 0.5, anchor = CENTER)

window.mainloop()
