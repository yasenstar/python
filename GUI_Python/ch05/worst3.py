from guizero import App, Text, Slider
from time import ctime

def update_date():
    the_date.value = ctime(date_slider.value)

app = App("Set the datae with the slider")
the_date = Text(app)
date_slider = Slider(app, start=0, end=99999999999, command=update_date)

app.display()