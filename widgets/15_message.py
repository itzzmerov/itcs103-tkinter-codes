import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")
window.title("ITCS103 TKINTER!")

messageVar = tk.Message(window, text='This is our Message!')
messageVar.config(bg='lightgreen')
messageVar.pack()

window.mainloop()