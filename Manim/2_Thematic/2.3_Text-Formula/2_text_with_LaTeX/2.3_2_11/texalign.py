from manim import *

class LaTeXAlignEnvironment(Scene):
    def construct(self):
        tex = MathTex(
            r"f(x) &= 3 + 2 + 1 \\ &= 5 + 1 \\ &= 6",
            font_size = 150,
            )
        self.add(tex)