from manim import *

class HeatDiagramPlot(Scene):
    def construct(self):
        ax = Axes(
            x_range = [0, 40, 5],
            y_range = [-8, 32, 5],
            x_length = 9,
            y_length = 6,
            x_axis_config = {
                "numbers_to_include": np.arange(0, 40, 5)
            },
            y_axis_config = {
                "numbers_to_include": np.arange(-5, 34, 5)
            }
        )

        labels = ax.get_axis_labels(
            x_label = MathTex("\Delta Q"),
            y_label = Tex("$T[^\circ C$]")
        )

        graph = ax.plot_line_graph(
            x_values = [0, 8, 38, 39],
            y_values = [20, 0, 0, -5]
        ).set_color(GREEN)

        self.add(ax, labels, graph)