# Imports
from guizero import App, Text, Waffle
from random import randint

# Constant
GRID_SIZE = 5

# Varibles

# Function
def add_dot():
    x, y = randint(0, GRID_SIZE-1), randint(0, GRID_SIZE-1)
    while board[x,y].dotty == True:
        x, y = randint(0, GRID_SIZE-1), randint(0, GRID_SIZE-1)
    board[x,y].dotty = True
    board.set_pixel(x,y,"red")
    board.after(1000, add_dot)

def destroy_dot(x,y):
    if board[x,y].dotty == True:
        board[x,y].dotty = False
        board.set_pixel(x,y,"green")

# App
app = App(title="Destroy the dots!")

instructions = Text(app, text="Click the dots to destroy them")
board = Waffle(
    app,
    height = GRID_SIZE,
    width = GRID_SIZE,
    color = "green",
    command = destroy_dot
)
board.after(1000, add_dot)

app.display()