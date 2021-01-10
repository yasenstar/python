from tkinter import *

root = Tk()
root.title("ch2_19")

html_jpg = PhotoImage(file="images/snow_river.gif")

label = Label(root, image = html_jpg)
label.pack()
print(type(label))

root.mainloop()
