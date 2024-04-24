# Imports
from guizero import App, Text, Waffle
from random import randint

# Constant
GRID_SIZE = 5

# Varibles

# Function
def add_dot():
    x, y = randint(0, GRID_SIZE-1), randint(0, GRID_SIZE-1)

# App
app = App(title="Destroy the dots!")

instructions = Text(app, text="Click the dots to destroy them")
board = Waffle(
    app,
    height = GRID_SIZE,
    width = GRID_SIZE,
    color = "green"
)

app.display()