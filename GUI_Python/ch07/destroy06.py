# Imports
from guizero import App, Text, Waffle
from random import randint

# Constant
GRID_SIZE = 5

# Varibles
score = 0

# Function
def add_dot():
    x, y = randint(0, GRID_SIZE-1), randint(0, GRID_SIZE-1)
    while board[x,y].dotty == True:
        x, y = randint(0, GRID_SIZE-1), randint(0, GRID_SIZE-1)
    board[x,y].dotty = True
    board.set_pixel(x,y,"red")
    board.after(1000, add_dot)

def destroy_dot(x,y):
    global score
    if board[x,y].dotty == True:
        board[x,y].dotty = False
        board.set_pixel(x,y,"green")
        score = score + 1
        score_display.value = "Your score is " + str(score)

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
score_display = Text(app, text="Your score is " + str(score))

app.display()