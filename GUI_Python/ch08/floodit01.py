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
moves_limit = 5

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
        
# ------------------------------
# App
# ------------------------------
app = App("Flood It")
app.display()