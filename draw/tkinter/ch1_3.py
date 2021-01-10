# ch1_2.py
from tkinter import *

root = Tk()
root.title("MyWindow")
root.geometry("500x400")
root.configure(bg='green')
# root.iconbitmap("images/mycoffee.ico")
root.mainloop()

"""
Traceback (most recent call last):
  File "/home/yasen/Documents/GitHub/python/draw/tkinter/ch1_3.py", line 8, in <module>
    root.iconbitmap("mycoffee.ico")
  File "/usr/lib/python3.8/tkinter/__init__.py", line 2071, in wm_iconbitmap
    return self.tk.call('wm', 'iconbitmap', self._w, bitmap)
_tkinter.TclError: bitmap "mycoffee.ico" not defined
"""