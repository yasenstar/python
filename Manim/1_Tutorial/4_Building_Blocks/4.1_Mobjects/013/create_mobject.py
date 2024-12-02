from manim import *

class CreatingMobjects(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait(3)
        self.remove(circle)
        self.wait(1.5)