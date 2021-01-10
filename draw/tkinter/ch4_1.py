from tkinter import *

def msgShow():
    label["text"] = "Hello World from Yasen"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"

root = Tk()
root.title("ch4_1")
label = Label(root)
btn = Button(root, text="print message", command = msgShow)
label.pack()
btn.pack()

root.mainloop()