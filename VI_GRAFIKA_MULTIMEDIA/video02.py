# use ffmplay to play the videos with tkinter

import tkinter as tk
import tkinter.ttk as ttk
import os

root = tk.Tk()

lb = tk.Listbox(root)
lb.pack()

for file in os.listdir():
    if file.endswith("C:\\Users\\tomast\\Videos\\shooting_training.mp4"):
        lb.insert(0, file)

root.mainloop()