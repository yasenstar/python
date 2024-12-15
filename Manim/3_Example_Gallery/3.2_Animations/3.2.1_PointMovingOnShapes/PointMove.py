from manim import *

class PointMovingOnShapes(Scene):
    def construct(self):
        circle = Circle(radius = 1, color = BLUE)
        self.play(GrowFromCenter(circle))

        dot1 = Dot()
        dot2 = dot1.copy().shift(RIGHT)
        self.add(dot1)
        self.play(Transform(dot1, dot2))

        line = Line([3,0,0], [5,0,0])
        self.add(line)

        self.play(MoveAlongPath(dot1, circle), run_time=3, rate_func = linear)

        self.play(Rotating(dot1, about_point = [2,0,0]), run_time = 2)

        self.play(Rotating(dot1, about_point = [3,0,0]), run_time = 2)

        self.wait()