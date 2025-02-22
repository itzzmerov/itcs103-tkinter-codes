import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")
window.title("Place Method Tutorial")

#Create a frame that expands according window size
pane = tk.Frame(window)
pane.pack(fill = BOTH, expand=True)

# button widgets which can also expand and fill
b1 = tk.Button(pane, text = "Click me !")
b1.pack(fill = BOTH, expand = True)

b2 = tk.Button(pane, text = "Click me too")
b2.pack(fill = BOTH, expand = True)

window.mainloop()