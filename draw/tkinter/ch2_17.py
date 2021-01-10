from tkinter import *

root = Tk()
root.title("ch2_6")

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
w = 300
h = 160
x = (screenWidth - w) / 2
y = (screenHeight - h) / 2
y = 200
root.geometry("%dx%d+%d+%d" % (w,h,x,y))

label = Label(root, bitmap="questhead", compound="right", text = "Hello World",
              relief="raised",
              fg='blue', bg='yellow',
              )
label.pack()
print(type(label))

root.mainloop()

"""
relief property:

flat    groove  raised  ridge   solid   sunken

"""