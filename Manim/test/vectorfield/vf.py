from manim import *

class BasicUsage(Scene):
    def construct(self):
        func = lambda pos: np.sin((pos[0] * UR + pos[1] * LEFT) - pos) / 3
        self.add(ArrowVectorField(func))