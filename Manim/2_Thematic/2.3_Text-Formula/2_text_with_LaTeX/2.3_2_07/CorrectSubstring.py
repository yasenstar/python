from manim import *

class CorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = \
            x^0 + x^1 + \frac{1}{2} x^2 + \
            \frac{1}{6}x^3 + ... + \cdots +\
            \frac{1}{n!} x^n + \cdots",
            # r"\frac{x^2+y^3}{z^(3+y)}",
            substrings_to_isolate="x"
        )
        equation.set_color_by_tex('x', RED)
        # equation[1].set_color(PURPLE)
        self.add(equation)