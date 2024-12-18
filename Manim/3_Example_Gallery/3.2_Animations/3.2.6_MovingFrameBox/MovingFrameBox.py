from manim import *

class MovingFrameBox(Scene):
    def construct(self):
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)",
            "=",
            "f(x)\\frac{d}{dx}g(x)",
            "+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text), run_time = 2)

        framebox1 = SurroundingRectangle(text[0], buff = .1).set_color(RED)

        self.play(Create(framebox1))
        self.wait()

        framebox2 = SurroundingRectangle(text[2], buff = .1).set_color(BLUE)
        framebox3 = SurroundingRectangle(text[4], buff = .1).set_color(GREEN)

        self.play(ReplacementTransform(framebox1, framebox2))
        self.wait()
        self.play(ReplacementTransform(framebox2, framebox3))
        self.wait()