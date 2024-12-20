from manim import *

class ArgMinExample(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10],
            y_range=[0,100,10],
            axis_config = {"include_tip": False}
        )
        labels = ax.get_axis_labels(
            x_label = "x",
            y_label = "f(x)"
        )

        t = ValueTracker(0)

        def func1(x):
            return 2 * (x - 5) ** 2
        
        graph1 = ax.plot(func1, color = MAROON)

        def func2(x):
            return (2 * (x + 1) ** 3) ** (0.7) - 7
        
        graph2 = ax.plot(func2, color = BLUE)

        initial_point1 = [
            ax.coords_to_point(t.get_value(), func1(t.get_value()))
        ]
        dot1 = Dot(point = initial_point1)

        dot1.add_updater(
            lambda x: x.move_to(
                ax.c2p(t.get_value(), func1(t.get_value()))
            )
        )
        x_space = np.linspace(*ax.x_range[:2],200)
        minimum_index = func1(x_space).argmin()

        self.add(ax, labels, graph1, graph2, dot1)
        self.play(t.animate.set_value(x_space[minimum_index]), run_time = 4)
        self.wait()