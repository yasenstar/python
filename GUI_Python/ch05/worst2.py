from guizero import App, Text

def flash_text():
    if title.visible:
        title.hide()
    else:
        title.show()

app = App("It is all gone wrong", bg="dark green")

title = Text(
    app,
    text="Some hard to read text",
    size=14,
    font="Comic Sans",
    color="green"
)

app.repeat(1000, flash_text)

app.display()