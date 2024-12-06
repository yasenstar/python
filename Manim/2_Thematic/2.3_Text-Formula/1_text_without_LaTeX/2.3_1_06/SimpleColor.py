from manim import *

class SimpleColor(Scene):
    def construct(self):
        col1 = Text("RED COLOR", color=RED).move_to(UP*2)
        col2 = Text("Another Color", color="#AAFFAA")
        col3 = Text("Blue Color", color="#0000FF").move_to(DOWN)
        self.add(col1, col2, col3)