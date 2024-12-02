from manim import *

class ExampleTransform(Scene):
    def construct(self):
        self.camera.background_color = GREEN_B
        m1 = Square().set_color(RED)
        m2 = Rectangle().set_color(BLUE).rotate(0.2)
        self.play(Transform(m1,m2))