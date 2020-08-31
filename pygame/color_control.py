# This comment is here for clarity reasons
# https://opensource.com/article/19/1/pygame-zero
color = [0,0,0]

def draw():
    screen.fill(tuple(color))

def update():
    color[0] = (color[0] + 1) % 256

def on_key_down(key, mod, unicode):
    color[1] = (color[1] + 2) % 256
    color[2] = (color[2] + 3) % 256