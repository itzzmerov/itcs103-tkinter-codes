import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")
window.title("ITCS103 TKINTER!")

spinBox = tk.Spinbox(window, from_=0, to=100)
spinBox.pack()

window.mainloop()