from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity = 0.5)
        self.play(Create(circle))