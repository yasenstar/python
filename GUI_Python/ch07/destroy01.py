# Imports
from guizero import App, Text, Waffle

# App
app = App(title="Destroy the dots!")

instructions = Text(app, text="Click the dots to destroy them")
board = Waffle(
    app,
    height = 5,
    width = 5,
    color = "green"
)

app.display()