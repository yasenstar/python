from manim import *

class ToyExample(Scene):
    def construct(self):
        organge_square = Square(color=ORANGE, fill_opacity=0.5)
        blue_circle = Circle(color=BLUE, fill_opacity = 0.5)

        self.add(organge_square)
        self.play(ReplacementTransform(organge_square, blue_circle, run_time=3))

        small_dot = Dot()

        small_dot.add_updater(lambda mob: mob.next_to(blue_circle, DOWN))

        self.play(Create(small_dot))
        
        self.play(blue_circle.animate.shift(UP))
        self.wait()

        self.play(FadeOut(blue_circle, run_time=4))