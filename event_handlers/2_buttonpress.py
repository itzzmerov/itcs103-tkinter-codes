import tkinter as tk

window = tk.Tk()

def handle_click(event):
    print("The button was clicked!")

button = tk.Button(window, text="Click me!")

button.bind("<Button-1>", handle_click)

button.pack()

window.mainloop()
