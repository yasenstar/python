from manim import *

class BooleanOperations(Scene):
    def construct(self):
        ellipse1 = Ellipse(
            width = 4.0,
            height = 5.0,
            color = BLUE,
            fill_opacity = 0.5,
            stroke_width = 10
        ).move_to(LEFT)
        ellipse2 = ellipse1.copy().set_color(color=RED).move_to(RIGHT)
        ellipse_shape_group = Group(ellipse1, ellipse2)
        bool_ops_text = MarkupText("<u>Boolean Operations</u>").next_to(ellipse_shape_group, UP * 3)
        ellipse_group = Group(ellipse1, ellipse2, bool_ops_text).move_to(LEFT * 3)
        self.play(FadeIn(ellipse_group))

        # boolean: intersection
        i = Intersection(ellipse1, ellipse2, color = GREEN, fill_opacity = 0.5)
        self.play(i.animate.scale(0.3).move_to(RIGHT * 2 + UP * 2))
        i_text = Text("Intersection", font_size = 23).next_to(i, UP)
        self.play(FadeIn(i_text))

        # boolean: union
        u = Union(ellipse1, ellipse2, color = ORANGE, fill_opacity = 0.5)
        self.play(u.animate.scale(0.3).move_to(RIGHT * 2 + DOWN * 2))
        u_text = Text("Union", font_size = 23).next_to(u, UP)
        self.play(FadeIn(u_text))

        # boolean: exclusion
        e = Exclusion(ellipse1, ellipse2, color = YELLOW, fill_opacity = 0.5)
        self.play(e.animate.scale(0.3).move_to(RIGHT * 5 + UP * 2))
        e_text = Text("Exclusion", font_size = 23).next_to(e, UP)
        self.play(FadeIn(e_text))

        # boolean: difference
        d = Difference(ellipse1, ellipse2, color = PINK, fill_opacity = 0.5)
        self.play(d.animate.scale(0.3).move_to(RIGHT * 5 + DOWN * 2))
        d_text = Text("Difference", font_size = 23).next_to(d, UP)
        self.play(FadeIn(d_text))