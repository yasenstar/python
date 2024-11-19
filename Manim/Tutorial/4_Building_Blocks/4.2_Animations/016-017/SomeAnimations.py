from manim import *

class SomeAnimations(Scene):
    def construct(self):
        square = Square()

        self.play(FadeIn(square))

        self.play(Rotate(square, PI/4))

        self.wait(1)

        self.play(Rotate(square, PI/4))

        self.play(FadeOut(square))

        self.wait(1)