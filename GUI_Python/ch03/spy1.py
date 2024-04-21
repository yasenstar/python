from guizero import App, Text, PushButton

def choose_name():
    print("Button is pressed!")

app = App("TOP SECRET")

title = Text(app, "Push the RED button to find out your spy name")

button = PushButton(app, choose_name, text="Tell me!")

app.display()