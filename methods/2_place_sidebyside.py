import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")
window.title("Place Method Tutorial")

pane = tk.Frame(window)
pane.pack(fill = BOTH, expand=True)

b1 = tk.Button(pane, text = "Click me !", background = "red", fg = "white")
b1.pack(side = LEFT, expand = True, fill = X)

b2 = Button(pane, text = "Click me too", background = "blue", fg = "white")
b2.pack(side = LEFT, expand = True, fill = X)

b3 = Button(pane, text = "I'm also button", background = "green", fg = "white")
b3.pack(side = LEFT, expand = True, fill = X)

window.mainloop()
