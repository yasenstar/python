from manim import *

class FontsExample(Scene):
    def construct(self):
        ft1 = Text("Nirmala UI", font = "Nirmala UI", font_size= 50).move_to(UP*2)
        ft2 = Text("Impact", font = "Impact", font_size = 60)
        self.add(ft1, ft2)