from manim import *

class FixedInFrameMObjectTest(ThreeDScene):
    def construct(self):
        axes1 = Axes()
        self.add_fixed_in_frame_mobjects(axes1)
        axes2 = ThreeDAxes()

        text3d = Text("This is a 3D text")
        self.add_fixed_in_frame_mobjects(text3d)
        text3d.to_corner(UL)

        self.set_camera_orientation(
            phi = 75 * DEGREES,
            theta = -45 * DEGREES
        )

        self.add(axes1.move_to(DR*2), axes2, text3d)
        
        self.wait()