from manim import *

class AddWithRunTimeScene(Scene):
    def construct(self):
        circles = VGroup(
            *[Circle(radius=0.5) for _ in range(30)]
        ).arrange_in_grid(6, 5)
        # circle = Circle(radius = 0.5)

        self.play(
            Succession(
                # Add(circle, run_time=0.5)
                *[Add(circle, run_time=0.2) for circle in circles]
            )
        )
        self.wait()