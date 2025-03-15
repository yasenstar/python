from manim import *

class FollowingGraphCamera(MovingCameraScene):
    def construct(self):

        ax = Axes(x_range=[-1,15], y_range=[-6,6])
        graph = ax.plot(lambda x: np.sin(x)*np.cos(x)*5, color=BLUE, x_range=[0, 4*PI])
        dot_1 = Dot(ax.i2gp(graph.t_min, graph))
        dot_2 = Dot(ax.i2gp(graph.t_max, graph))
        moving_dot = Dot(ax.i2gp(graph.t_min, graph), color=ORANGE)
        self.add(ax, graph, dot_1, dot_2, moving_dot)

        self.camera.frame.save_state()

        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.add_updater(update_curve)
        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear))
        self.camera.frame.remove_updater(update_curve)
        
        self.play(Restore(self.camera.frame))