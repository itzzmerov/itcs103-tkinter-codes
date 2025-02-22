import tkinter as tk
from tkinter import ttk
import time

window = tk.Tk()
window.geometry("300x300")
window.title("ITCS103 TKINTER!")

def start_progress():
    progress.start()

    # Simulate a task that takes time to complete
    for i in range(101):
      # Simulate some work
        time.sleep(0.05)  
        progress['value'] = i
        # Update the GUI
        window.update_idletasks()  
    progress.stop()

# Create a progressbar widget
progress = ttk.Progressbar(window, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=20)

# Button to start progress
start_button = tk.Button(window, text="Start Progress", command=start_progress)
start_button.pack(pady=10)

window.mainloop()