import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")
window.title("ITCS103 TKINTER!")

# This is to hold the chosen boxes
var1 = IntVar()
var2 = IntVar()

# This is the checkboxes itself
cb1 = tk.Checkbutton(window, text="Basketball", variable=var1) #variable is used to push the data to the IntVar()
cb2 = tk.Checkbutton(window, text="Volleyball", variable=var2)
cb1.pack()
cb2.pack()

window.mainloop()