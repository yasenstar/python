from manim import *

class OpeningManim(Scene):
    def construct(self):
        # title = Tex(r"This is some \LaTex")
        # basel = MathTex(r"\sum")
        title = Text("This is some LaTex")
        basel = Text("Sum of a Formula")
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeIn(basel, shift = DOWN)
        )
        self.wait()

        transform_title = Text("That was a transform")
        transform_title.to_corner(UL)
        self.play(
            Transform(title, transform_title),
            LaggedStart(
                *[FadeOut(obj, shift=DOWN) for obj in basel]
            )
        )
        self.wait()

        grid = NumberPlane()
        grid_title = Text("This is a grid", font_size = 72)
        grid_title.move_to(transform_title)
        self.add(grid, grid_title)
        self.play(
            FadeOut(title),
            FadeIn(grid_title, shift=UP),
            Create(grid, run_time=3, lag_ratio=0.1)
        )
        self.wait()

        grid_transform_title = Text(
            "That was a non-linear function\n applied to the grid"
        )
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.animate.apply_function(
                lambda p: p + np.array(
                    [
                        np.sin(p[1]),
                        np.sin(p[0]),
                        0
                    ]
                )
            ),
            run_time = 3,
        )
        self.wait()
        self.play(Transform(grid_title, grid_transform_title))
        self.wait()