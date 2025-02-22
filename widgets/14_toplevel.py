import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")
window.title("This is the main window")

top = tk.Toplevel()
top.geometry("300x300")
top.title("This is toplevel")

window.mainloop()