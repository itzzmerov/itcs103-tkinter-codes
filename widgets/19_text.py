import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")
window.title("ITCS103 TKINTER!")

textBox = tk.Text(window, height=5, width=30)
textBox.pack()
textBox.insert(END, 'BSIT Lang Malakas \nIT DAY sa March')

window.mainloop()