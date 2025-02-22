import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")
window.title("ITCS103 TKINTER!")

# This is to hold the chosen boxes
gender = IntVar()

# This is the checkboxes itself
rb1 = tk.Radiobutton(window, text="male", variable=gender, value="male")
rb2 = tk.Radiobutton(window, text="female", variable=gender, value="female")
rb1.pack()
rb2.pack()

window.mainloop()