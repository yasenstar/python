from manim import *

class PointWithTrace(Scene):
    def construct(self):
        
        
        # # line = Line(ORIGIN, LEFT * 2).set_color(BLUE)
        # path = VMobject()
        # dot = Dot(LEFT * 2)
        # path.set_points_as_corners([dot.get_center(), dot.get_center()])
        # def update_path(path):
        #     previous_path = path.copy()
        #     previous_path.add_points_as_corners([dot.get_center()])
        #     path.become(previous_path)

        # path.add_updater(update_path)

        # self.add(path, dot)

        # self.play(Rotating(dot, radians = PI, about_point = ORIGIN, run_time = 2))
        # self.wait()

        # self.play(dot.animate.shift(UP * 2))
        # self.play(dot.animate.shift(LEFT * 4))
        # self.play(dot.animate.shift(DOWN * 2))
        # self.wait()

        path = VMobject()
        dot = Dot()
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)
        self.add(path, dot)
        self.play(Rotating(dot, radians=PI, about_point=RIGHT, run_time=2))
        # self.wait()
        self.play(dot.animate.shift(UP))
        self.play(dot.animate.shift(LEFT))
        self.wait()