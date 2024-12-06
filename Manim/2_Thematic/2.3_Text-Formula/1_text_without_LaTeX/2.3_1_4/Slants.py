from manim import *

class SlantsExample(Scene):
    def construct(self):
        a = Text("Normal", slant=NORMAL).move_to(UP*2)
        b = Text("Italic", slant=ITALIC).move_to(UP*1)
        c = Text("Oblique", slant=OBLIQUE)
        self.add(a,b,c)