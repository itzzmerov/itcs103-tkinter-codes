import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")
window.title("Place Method Tutorial")

l1 = Label(window, text = "First:")
l2 = Label(window, text = "Second:")

# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row=0, column=0, sticky= W, pady=2)
l2.grid(row=1, column=0, sticky= W, pady=2)

# entry widgets, used to take entry from user
e1 = tk.Entry(window)
e2 = tk.Entry(window)

# this will arrange entry widgets
e1.grid(row = 0, column = 1, pady = 2)
e2.grid(row = 1, column = 1, pady = 2)

window.mainloop()
