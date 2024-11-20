from manim import *

class RunTime(Scene):
    def construct(self):
        square = Square().set_fill(BLUE, opacity=1.0)
        self.add(square)
        self.play(square.animate.shift(UP).rotate(PI/3), run_time=5)
        self.wait(2)