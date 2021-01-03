from tkinter import *

def msgShow():
    label["text"] = "Hello World from Yasen"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"

root = Tk()
root.title("ch4_3")
label = Label(root)
btn1 = Button(root, text="print message", command = msgShow)
btn2 = Button(root, text="close", command=root.destroy)
label.pack()
btn1.pack(side="left")
btn2.pack(side="right")

root.mainloop()