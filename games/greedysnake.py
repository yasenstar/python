from turtle import *
from random import randrange
from freegames import *

snake = [vector(10,0)]
food = vector(0,0)
aim = vector(0,10)

def change(x,y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundary"
    return -200 < head.x < 200 and -200 < head.y < 200

def move():
    "Move snake forward one step."
    head = snake[-1].copy()
    head.move(aim)

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
    
    clear()

    for body in snake:
        square(body.x, body.y, 9, 'purple')
    
    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 300)

def main():
    # setup(600, 500, 800, 0)
    setup(1.0, 1.0)
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: change(10,0), "Right")
    onkey(lambda: change(-10,0),"Left")
    onkey(lambda: change(0,10), "Up")
    onkey(lambda: change(0,-10),"Down")
    move()
    done()

main()