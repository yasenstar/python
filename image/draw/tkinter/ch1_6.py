from tkinter import *

root = Tk()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
w = 300
h = 160
x = (screenWidth - w) / 2
y = (screenHeight - h) / 2
y = 200
root.geometry("%dx%d+%d+%d" % (w,h,x,y))
root.mainloop()