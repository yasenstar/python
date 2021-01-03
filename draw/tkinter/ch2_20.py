from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("ch2_20")
root.geometry("600x400")

hellotext = "Hello World"
image = Image.open("images/snow_river.gif")
snow_river = ImageTk.PhotoImage(image)
label = Label(root, text=hellotext, image = snow_river,
            bg="lightyellow", compound="left")
label.pack()
print(type(label))

root.mainloop()

# $ pip install pillow
# $ sudo apt install python3-pil.imagetk
# note: the ImageTk need installed separately