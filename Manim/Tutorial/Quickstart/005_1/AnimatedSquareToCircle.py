from manim import *

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        
        self.play(Create(square))
        self.play(square.animate.set_fill(GREEN, opacity=0.2))
        self.play(square.animate.rotate(PI / 3))
        self.play(Transform(square, circle))
        self.play(square.animate.set_fill(YELLOW, opacity=0.5))