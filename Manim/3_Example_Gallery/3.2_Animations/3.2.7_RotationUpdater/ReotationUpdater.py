from manim import *

class RotationUpdater(Scene):
    def construct(self):
        def updater_forth(mobj, dt):
            mobj.rotate_about_origin(dt)
        def updater_back(mobj, dt):
            mobj.rotate_about_origin(-dt)
        
        line_static = Line(ORIGIN, LEFT*2).set_color(RED)
        line_moving = Line(ORIGIN, LEFT).set_color(YELLOW)
        self.add(line_static, line_moving)

        line_moving.add_updater(updater_forth)
        self.wait(6.25)

        line_moving.remove_updater(updater_forth)
        self.wait(2)

        line_moving.add_updater(updater_back)
        self.wait(6.25)

        line_moving.remove_updater(updater_back)
        self.wait(2)