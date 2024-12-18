from manim import *

class SinAndCosFunctionPlot(Scene):
    def construct(self):

        self.add(NumberPlane())

        axes = Axes(
            x_range = [-10, 11.5, 1],
            y_range = [-1.5, 1.5, 1],
            x_length = 10,
            axis_config = {"color": GREEN},
            x_axis_config = {
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            # tips = False,
        )

        self.add(axes)

        axes_labels = axes.get_axis_labels()

        self.add(axes_labels)

        sin_graph = axes.plot(lambda x: np.sin(x), color = BLUE)
        cos_graph = axes.plot(lambda x: np.cos(x), color = RED)
        sin_plus_cos_graph = axes.plot(lambda x: np.sin(x)**2+np.cos(x), color = GREEN)

        sin_label = axes.get_graph_label(
            sin_graph,
            "sin(x)"
        )

        cos_label = axes.get_graph_label(
            cos_graph,
            "cos(x)"
        )

        self.add(sin_graph, cos_graph, sin_label, cos_label, sin_plus_cos_graph)

        vert_line_sin = axes.get_vertical_line(
            axes.i2gp(TAU, sin_graph),
            color = PINK,
            line_func = Line
        )

        vert_line_cos = axes.get_vertical_line(
            axes.i2gp(TAU, cos_graph),
            color = YELLOW,
            line_func = Line
        )

        self.add(vert_line_sin, vert_line_cos)

        line_label = axes.get_graph_label(
            cos_graph,
            "x=2\pi",
            x_val = TAU,
            direction = UR,
            color = YELLOW
        )

        self.add(line_label)