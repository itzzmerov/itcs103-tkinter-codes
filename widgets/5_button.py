import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")
window.title("ITCS103 TKINTER!")

button = tk.Button(window, text="Destroy!", width=25, command=window.destroy)
button.pack()

window.mainloop()