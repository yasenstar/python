# -*- coding: utf-8 -*-
from tkinter import *

window = Tk()
label = Label(window, text = "Welcome to Python")
button = Button(window, text = "Click Me", command=window.destroy)
label.pack()
button.pack()

window.mainloop()