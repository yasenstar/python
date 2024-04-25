# ------------------------------
# Imports
# ------------------------------

from guizero import App, Waffle, Text, PushButton, info
import random

# ------------------------------
# Variables
# ------------------------------

colours = ["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"]
board_size = 14
moves_limit = 50
moves_taken = 0

# ------------------------------
# Functions
# ------------------------------

# Recursively floods adjacent squares
  
def flood(x, y, target, replacement):
    # Algorithm from https://en.wikipedia.org/wiki/Flood_fill
    if target == replacement:
        return False
    if board.get_pixel(x, y) != target:
        return False
    board.set_pixel(x, y, replacement)
    if y+1 <= board_size-1:   # South
        flood(x, y+1, target, replacement)
    if y-1 >= 0:            # North
        flood(x, y-1, target, replacement)
    if x+1 <= board_size-1:    # East
        flood(x+1, y, target, replacement)
    if x-1 >= 0:            # West
        flood(x-1, y, target, replacement)

# Check whether all squares are the same
def all_squares_are_the_same():
    squares = board.get_all()
    if all(colour == squares[0] for colour in squares):
        return True
    else:
        return False

def win_check():
    global moves_taken
    moves_taken = moves_taken + 1
    steps_left.value = "You have " + str(moves_limit - moves_taken) + " steps left."
    print(moves_taken)
    if moves_taken < moves_limit:
        if all_squares_are_the_same():
            win_text.value = "Congratulation, You Win!"
            palette.disable()
    else:
        win_text.value = "You lose :("
        palette.disable()

def fill_board():
    for x in range(board_size):
        for y in range(board_size):
            board.set_pixel(x, y, random.choice(colours))

def init_palette():
    for colour in colours:
        palette.set_pixel(colours.index(colour), 0, colour)

def start_flood(x, y):
    flood_colour = palette.get_pixel(x,y)
    target = board.get_pixel(0,0)
    flood(0, 0, target, flood_colour)
    win_check()

def show_info():
    if instruction.value == "":
        instruction.value = "This game aims to flood the board with all squares the same color."
    else:
        instruction.value = ""
        
# ------------------------------
# App
# ------------------------------
app = App("Flood It")

info = PushButton(app, text="See Instructure", command=show_info)

board = Waffle(app, width=board_size, height=board_size, pad=0)
palette = Waffle(app, width=8, height=1, dotty=True, command=start_flood)

steps_left = Text(app, text = "You have " + str(moves_limit - moves_taken) + " steps left.")
instruction = Text(app, text="")
win_text = Text(app)

fill_board()
init_palette()

app.display()