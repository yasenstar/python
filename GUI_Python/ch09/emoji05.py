# Imports
import os
from random import shuffle, randint
from guizero import App, Box, Picture, PushButton, Text

# Variables

# Set the path to the emoji folder on your computer
emojis_dir = "D:\\GitHub\\python\\GUI_Python\\ch09\\emojis"
emojis = [os.path.join(emojis_dir, f) for f in os.listdir(emojis_dir)]
shuffle(emojis)
# print(emojis)

# Functions
def setup_round():
    for picture in pictures:
        picture.image = emojis.pop()
    
    for button in buttons:
        button.image = emojis.pop()
        button.update_command(match_emoji, args=[False])
    
    matched_emoji = emojis.pop()
    
    random_picture = randint(0,14)
    pictures[random_picture].image = matched_emoji
    
    random_button = randint(0,14)
    buttons[random_button].image = matched_emoji
    
    buttons[random_button].update_command(match_emoji, args=[True])
    
    timer.value="5"
    
    pictures_box.visible=True
    buttons_box.visible=True
    timer.visible=True
    score.visible=True
    result.visible=False
    restart.visible = False

def match_emoji(matched):
    if matched:
        result.value = "correct"
        score.value = int(score.value) + 1
    else:
        result.value = "incorrect"
        score.value = int(score.value) - 1
    setup_round()

def reduce_time():
    timer.value = int(timer.value) - 1
    if int(timer.value) < 0:
        result.value = "Game over! Score = " + score.value
        result.visible=True
        pictures_box.hide()
        buttons_box.hide()
        timer.hide()
        score.hide()
        restart.visible = True

# App
app = App("emoji match")

score = Text(app, text="0")
timer = Text(app, text="5")

pictures_box = Box(app, layout="grid")
buttons_box = Box(app, layout="grid")

pictures = []
buttons = []

for x in range(0,5):
    for y in range(0,3):
        picture = Picture(pictures_box, grid=[x,y])
        pictures.append(picture)
        button = PushButton(buttons_box, grid=[x,y])
        buttons.append(button)

result = Text(app)

app.repeat(1000, reduce_time)

restart = PushButton(app, text="Restart Game", command=setup_round)
restart.visible = False

setup_round()

app.display()