from manim import *

class Textt2cExample(Scene):
    def construct(self):
        t2c1 = Text("Hello", t2c={'[1:-2]': BLUE}).move_to(LEFT)
        t2c2 = Text("World!", t2c={"rld":RED}).next_to(t2c1, RIGHT)
        self.add(t2c1, t2c2)