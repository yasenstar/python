from guizero import App, Text, PushButton
from random import choice

def choose_name():
    # print("Button is pressed!")
    first_names = ["Barbar", "Woody", "Tiberius", "Smokey", "Jennifer", "Rugy", "Yasen"]
    last_names = ["Spindleshands", "Mysterioso", "Dungeon", "Catseye", "Zhao", "Darkmeyer", "Flamingobreath"]

    spy_name = choice(first_names) + " " + choice(last_names)
    # print(spy_name)
    name.value = spy_name

app = App("TOP SECRET")

title = Text(app, "Push the RED button to find out your spy name")

button = PushButton(app, command=choose_name, text="Tell me!")
button.bg = "red"
button.text_color = "white"
button.text_size = 30

name = Text(app, text="")
name.text_size = 30

app.display()