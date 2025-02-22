import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")
window.title("ITCS103 TKINTER!")

canvas = tk.Canvas(window, width=40, height=60)
canvas.pack()
canvas_height = 20
canvas_width = 200
y = int(canvas_height / 2)
canvas.create_line(0, y, canvas_width, y)

window.mainloop()