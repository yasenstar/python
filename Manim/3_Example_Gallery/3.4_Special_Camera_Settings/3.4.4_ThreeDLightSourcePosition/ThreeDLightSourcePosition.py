from manim import *

class ThreeDLightSourcePosition(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        sphere = Surface(
            lambda u, v: np.array(
                [
                    1.5 * np.cos(u) * np.cos(v),
                    1.5 * np.cos(u) * np.sin(v),
                    1.5 * np.sin(u)
                ]
            ),
            v_range = [0, TAU],
            u_range = [-PI / 2, PI / 2],
            checkerboard_colors = [GREEN_D, GREEN_E],
            resolution = (15, 32)
        )
        self.set_camera_orientation(
            phi = 75 * DEGREES,
            theta = 30 * DEGREES
        )
        self.renderer.camera.light_source.move_to(2 * IN)
        self.add(axes, sphere)
        self.wait()