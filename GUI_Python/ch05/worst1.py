from guizero import App, Text

app = App("It is all gone wrong", bg="dark green")

title = Text(
    app,
    text="Some hard to read text",
    size=14,
    font="Comic Sans",
    color="green"
)

app.display()