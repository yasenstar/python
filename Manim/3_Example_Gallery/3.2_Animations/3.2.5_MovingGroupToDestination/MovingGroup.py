from manim import *

class MovingGroupToDestination(Scene):
    def construct(self):

        numberplane = NumberPlane()

        group = VGroup(
            Dot(LEFT * 2),
            Dot(LEFT),
            Dot(ORIGIN, color = RED),
            Dot(RIGHT),
            Dot(RIGHT * 2)
        ).scale(2.0)

        dest = Dot(
            [4,-3,0],
            color = YELLOW
        )

        self.add(numberplane, group, dest)

        self.play(group.animate.shift(dest.get_center() - group[1].get_center()), run_time = 5)
        self.wait()