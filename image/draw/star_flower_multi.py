import turtle
import time

turtle.color("red", "yellow")
turtle.begin_fill()
for _ in range(50):
    turtle.forward(200)
    turtle.left(150)
    turtle.forward(30)
    turtle.right(150)
    turtle.forward(30)
    turtle.left(170)
    turtle.end_fill()

turtle.mainloop()