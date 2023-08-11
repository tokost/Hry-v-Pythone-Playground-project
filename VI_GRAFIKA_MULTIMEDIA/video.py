import os
from tkinter import *

app = Tk()
app.title('Video Player')

Fcanvas = Canvas(bg="black", height=600, width=170)


def snd1():
    os.system("C:\\Users\\tomast\\Videos\\Dalajlama.mp4")

var = IntVar()

rb1 = Radiobutton(app, text= "Play Video", variable = var, value=1, command=snd1)
rb1.pack(anchor = W)
Fcanvas.pack()
app.mainloop()