from tkinter import *

def yellow():
    root.config(bg="yellow")

def blue():
    root.config(bg="blue")

root = Tk()
root.title("color bg")
root.geometry("500x300")

snowGif = PhotoImage(file="images/snow_river.gif")

# exitbtn = Button(root, image=snowGif, command = root.destroy)
exitbtn = Button(root, text = "Exit", command = root.destroy)
bluebtn = Button(root, text="Blue", command = blue)
yellowbtn = Button(root, text="Yellow", command = yellow)

exitbtn.pack(anchor=S, side="right", padx=5, pady=5)
bluebtn.pack(anchor=S, side="right", padx=5, pady=5)
yellowbtn.pack(anchor=S, side="right", padx=5, pady=5)

root.mainloop()