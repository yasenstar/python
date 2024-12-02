from manim import *

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        
        square = Square()
        square.set_fill(BLUE, opacity=0.5)
        
        square2 = Square()
        square2.set_fill(YELLOW, opacity=0.5)
        
        circle.next_to(square, DOWN, buff=1.0)
        square2.next_to(square, RIGHT, buff=0.5)
        self.play(Create(circle), Create(square), Create(square2))