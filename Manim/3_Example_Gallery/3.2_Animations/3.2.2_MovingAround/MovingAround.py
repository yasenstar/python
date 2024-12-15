from manim import *

class MovingAround(Scene):
    def construct(self):
        square = Square(color = BLUE, fill_opacity = 1)

        self.play(square.animate.shift(LEFT*2), run_time = 1)
        # self.play(square.animate.shift(UP*2), run_time = 1)
        # self.play(square.animate.shift(RIGHT*2), run_time = 1)
        # self.play(square.animate.shift(DOWN*2), run_time = 1)

        self.play(square.animate.set_fill(RED).shift(UP*2), run_time = 4)
        self.play(square.animate.shift(RIGHT*2).set_fill(GREEN), run_time = 4)

        self.play(square.animate.scale(0.3).set_fill(YELLOW), run_time = 4)
        self.play(square.animate.scale(2).set_fill(WHITE), run_time = 4)

        self.play(square.animate.rotate(0.4).scale(3).set_fill(BLUE).shift(DOWN*3), run_time = 4)