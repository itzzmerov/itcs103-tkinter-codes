import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")
window.title("ITCS103 TKINTER!")

listBox = tk.Listbox(window) # Main panel for list box
listBox.insert(1, "Python") # Add items in list box
listBox.insert(2, "HTML")
listBox.insert(3, "CSS")
listBox.insert(4, "JavaScript")

listBox.pack()

window.mainloop()