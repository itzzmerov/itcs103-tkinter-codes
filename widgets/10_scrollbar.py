import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")
window.title("ITCS103 TKINTER!")

scrollBar = tk.Scrollbar(window)
scrollBar.pack(side=RIGHT, fill=Y)
myList = tk.Listbox(window, yscrollcommand=scrollBar.set)

for line in range(100):
    myList.insert(END, "This is line number" + str(line))
    
myList.pack(side=LEFT, fill=BOTH)
scrollBar.config(command=myList.yview)

window.mainloop()