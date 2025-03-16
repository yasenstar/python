from manim import *

class ThreeDSurfacePlot(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(
            phi = 75 * DEGREES,
            theta = -30 * DEGREES
        )

        resolution_fa = 24

        axes = ThreeDAxes()

        def param_gauss(u, v):
            x = u
            y = v
            sigma, mu = 0.4, [0.0, 0,0]
            d = np.linalg.norm(
                np.array(
                    [
                        x - mu[0],
                        y - mu[1]
                    ]
                )
            )
            z = np.exp(-(d ** 2 / (2.0 * sigma ** 2)))
            return np.array([x, y, z])
        
        gauss_plane = Surface(
            param_gauss,
            v_range = [-2, +2],
            u_range = [-2, +2],
            resolution = (resolution_fa*5, resolution_fa)
        )

        gauss_plane.scale(2, about_point=ORIGIN)
        gauss_plane.set_style(fill_opacity = 1, stroke_color = GREEN)
        gauss_plane.set_fill_by_checkerboard(ORANGE, BLUE, opacity = 0.5)

        self.add(axes, gauss_plane)
        # self.wait()