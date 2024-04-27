# Imports
import os
from random import shuffle
from guizero import App, Box, Picture, PushButton

# Variables

# Set the path to the emoji folder on your computer
emojis_dir = "D:\\GitHub\\python\\GUI_Python\\ch09\\emojis"
emojis = [os.path.join(emojis_dir, f) for f in os.listdir(emojis_dir)]
shuffle(emojis)

print(emojis)