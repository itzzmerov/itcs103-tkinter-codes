import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")
window.title("ITCS103 TKINTER!")

menu = tk.Menu(window)
window.config(menu=menu) # Configure Menu in Window

filemenu = Menu(menu) # Created menu for File
menu.add_cascade(label='File', menu=filemenu) # Add dropdown
filemenu.add_command(label='New') # Add commands or choices
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

window.mainloop()