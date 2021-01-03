from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("ch2_19_1")
root.geometry("600x400")

image = Image.open("images/snow_river.gif")
snow_river = ImageTk.PhotoImage(image)
label = Label(root, image = snow_river)
label.pack()
print(type(label))

root.mainloop()

# $ pip install pillow
# $ sudo apt install python3-pil.imagetk
# note: the ImageTk need installed separately