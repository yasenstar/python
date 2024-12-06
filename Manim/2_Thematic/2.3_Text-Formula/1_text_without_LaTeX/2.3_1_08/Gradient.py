from manim import *

class GradientExample(Scene):
    def construct(self):
        t1 = Text("Hello", gradient=(RED, BLUE, GREEN), font_size=70).move_to(UP)
        t2 = Text("Hello WORLD", gradient=(RED, BLUE, GREEN, YELLOW, RED), font_size=90)

        self.add(t1,t2)