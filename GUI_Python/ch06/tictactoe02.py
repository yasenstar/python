# Imports ------------------
from guizero import App, Box, PushButton

# Functions ----------------

# Variables ----------------

# App ----------------------
app = App(title="Tic Tac Toe")

board = Box(app, layout="grid")

for x in range(3):
    for y in range(3):
        button = PushButton(board, text="", grid=[x,y], width=3)

app.display()