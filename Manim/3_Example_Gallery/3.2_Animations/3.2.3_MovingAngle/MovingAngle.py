from manim import *

class MovingAngle(Scene):
    def construct(self):
        line_static = Line(LEFT, RIGHT)
        line_moving = Line(LEFT, RIGHT)
        line_ref = line_moving.copy()

        theta_tracker = ValueTracker(110)

        line_moving.rotate(
            theta_tracker.get_value() * DEGREES,
            about_point = LEFT
        )

        a = Angle(line_static, line_moving, radius = 0.5, other_angle = False)

        tex = MathTex(r"\theta").move_to(
            Angle(
                line_static,
                line_moving,
                radius = 0.5 + 5 * SMALL_BUFF,
                other_angle = False
            ).point_from_proportion(0.5)
        )

        self.add(line_static, line_moving, a, tex)
        self.wait()

        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES,
                about_point = LEFT
            )
        )

        a.add_updater(
            lambda x: x.become(
                Angle(line_static, line_moving, radius = 0.5, other_angle = False)
            )
        )

        tex.add_updater(
            lambda x: x.move_to(
                Angle(
                    line_static,
                    line_moving,
                    radius = 0.5 + 5 * SMALL_BUFF,
                    other_angle = False
                ).point_from_proportion(0.5)
            )
        )

        self.play(theta_tracker.animate.set_value(40))
        self.play(theta_tracker.animate.set_value(140))
        self.play(tex.animate.set_color(RED))
        self.play(theta_tracker.animate.increment_value(240))
        self.play(theta_tracker.animate.set_value(300))