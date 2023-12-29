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

label = Label(root, text = "I like tkinter",
              fg='blue', bg='yellow',
              height=3, width=15,
              anchor = 'center',
              wraplength = 41)
label.pack()
print(type(label))

root.mainloop()

"""
nw    n     ne
w   center   e
sw    s     se

if using capital, no need "", e.g. SE
"""