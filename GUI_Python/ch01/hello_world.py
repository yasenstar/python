from guizero import App, Text

app = App(title="Hello World with GUI")

message1 = Text(app, text="I love programming in Python!")

message2 = Text(app, text="Welcom to the GUI app!")

app.display()