import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")
window.title("ITCS103 TKINTER!")

mb = tk.Menubutton(window, text='File')
mb.grid()  # Created grid for selections
mb.menu = Menu ( mb, tearoff = 0 ) 
mb["menu"] = mb.menu 
cVar = IntVar() 
aVar = IntVar() 
mb.menu.add_checkbutton ( label ='Contact', variable = cVar ) 
mb.menu.add_checkbutton ( label = 'About', variable = aVar ) 
mb.pack() 

window.mainloop()