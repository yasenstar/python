from manim import *

class t2gExample(Scene):
    def construct(self):
        t2g1 = Text(
            "Hello",
            t2g = {
                '[1:-1]':(RED, GREEN)
            },
            font_size=90
        ).move_to(LEFT)

        t2g2 = Text(
            "World!",
            t2g = {
                'Worl':(BLUE, YELLOW, GREEN)
            },
            font_size=70
        ).next_to(t2g1, RIGHT)

        self.add(t2g1, t2g2)