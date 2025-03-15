from manim import *

class ThreeDCameraRotation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(
            phi = 75 * DEGREES,
            theta = 30 * DEGREES
        )
        circle = Circle(color = BLUE)
        self.add(axes, circle)

        self.begin_ambient_camera_rotation(rate=1.5)
        self.wait()
        self.wait()
        self.stop_ambient_camera_rotation()

        self.move_camera(
            phi = 125 * DEGREES,
            theta = -45 * DEGREES
        )

        self.wait()