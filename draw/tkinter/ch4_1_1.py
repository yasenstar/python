from tkinter import *

def msgShow():
    label.config(text = "Hello World from Yasen", bg = "lightyellow", fg = "blue")

root = Tk()
root.title("ch4_1_1 label config")
label = Label(root)
btn = Button(root, text="print message", command = msgShow)
label.pack()
btn.pack()

root.mainloop()