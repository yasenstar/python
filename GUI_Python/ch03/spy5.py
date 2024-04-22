from guizero import App, Text, PushButton
from random import choice

first_names = ["Barbar", "Woody", "Tiberius", "Smokey", "Jennifer", "Rugy", "Yasen"]
last_names = ["Spindleshands", "Mysterioso", "Dungeon", "Catseye", "Zhao", "Darkmeyer", "Flamingobreath"]

def choose_name(a,b):
    # print("Button is pressed!")
    spy_name = choice(a) + " " + choice(b)
    # print(spy_name)
    name.value = spy_name

app = App("TOP SECRET")

title = Text(app, "Push the RED button to find out your spy name")

button = PushButton(app, command = lambda:choose_name(first_names,last_names), text="Tell me!")
button.bg = "red"
button.text_color = "white"
button.text_size = 30

name = Text(app, text="")
name.text_size = 30

app.display()