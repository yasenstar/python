from manim import *

class ThreeDCameraIllusionRotation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(
            phi = 75 * DEGREES,
            theta = 30 * DEGREES
        )
        circle = Circle(color = BLUE)
        self.add(axes, circle)

        self.begin_3dillusion_camera_rotation(rate=2)
        self.wait(PI/2)
        self.stop_3dillusion_camera_rotation()

        self.move_camera(
            phi = 125 * DEGREES,
            theta = -45 * DEGREES
        )

        self.wait()