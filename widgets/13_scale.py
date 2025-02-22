import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")
window.title("ITCS103 TKINTER!")

horiScale = tk.Scale(window, from_=0, to=50)
horiScale.pack()
vertiScale = tk.Scale(window, from_=0, to=100, orient=HORIZONTAL)
vertiScale.pack()

window.mainloop()