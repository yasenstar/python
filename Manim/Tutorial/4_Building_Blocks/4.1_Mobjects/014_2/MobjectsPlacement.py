from manim import *

class MobjectsPlacement(Scene):
    def construct(self):
        circle = Circle()
        square = Square().move_to(RIGHT * 2).move_to(DOWN*3)
        triangle = Triangle()
        
        circle.move_to(LEFT * 3)
        
        # square.next_to(circle, UP)
        
        triangle.align_to(circle, LEFT)
        
        self.add(circle, square, triangle)
        self.wait(1)