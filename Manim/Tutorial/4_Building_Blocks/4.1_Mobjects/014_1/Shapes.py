from manim import *

class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()
        
        circle.shift(LEFT)
        circle.shift(UP)
        square.shift(UP)
        triangle.shift(RIGHT)
        
        self.add(circle, square, triangle)
        self.wait(1)