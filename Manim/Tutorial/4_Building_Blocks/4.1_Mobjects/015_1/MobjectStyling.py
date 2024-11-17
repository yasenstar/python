from manim import *

class MobjectStyling(Scene):
    def construct(self):
        circle = Circle().move_to(LEFT*0.5)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)
        
        circle.set_stroke(color=GREEN, width=40)
        square.set_fill(YELLOW, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.75)
        triangle.set_stroke(color=RED, width=30)
        
        # square.set_color(BLUE)
        
        self.add(circle, square, triangle)
        self.wait(1)