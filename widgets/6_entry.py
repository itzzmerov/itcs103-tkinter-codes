import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")
window.title("ITCS103 TKINTER!")

label = tk.Label(window, text="Username:")
label.pack()
entry = tk.Entry()
entry.pack()

window.mainloop()