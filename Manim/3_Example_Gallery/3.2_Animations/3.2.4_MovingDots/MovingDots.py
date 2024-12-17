from manim import *

class MovingDots(Scene):
    def construct(self):
        d1 = Dot(color = BLUE)
        d2 = Dot(color = GREEN).move_to(RIGHT)
        line = Line(d1.get_center(), d2.get_center()).set_color(PURPLE)

        x = ValueTracker(0)
        y = ValueTracker(0)

        d1.add_updater(
            lambda z: z.set_x(x.get_value())
        )

        d2.add_updater(
            lambda z: z.set_y(y.get_value())
        )

        line.add_updater(
            lambda z: z.become(
                Line(d1.get_center(), d2.get_center())
            )
        )

        self.add(line, d1, d2)
        self.wait()
        self.play(x.animate.set_value(5), run_time=3)
        self.wait()
        self.play(y.animate.set_value(3), run_time=3)
        self.wait()