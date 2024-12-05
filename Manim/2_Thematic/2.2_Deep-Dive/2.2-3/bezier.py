from manim import *

class VMobjectDemo(Scene):
    def construct(self):
        plane = NumberPlane()
        my_vmobject = VMobject(color=GREEN)
        my_vmobject.points = [
            np.array([-2, -1, 0]),
            np.array([-3, 1, 0]),
            np.array([0, 3, 0]),
            np.array([1, 3, 0]),
            np.array([1, 3, 0]),
            np.array([0, 1, 0]),
            np.array([4, 3, 0]),
            np.array([4, -2, 0])
        ]
        handles = [
            Dot(point, color=RED) for point in
            [
                [-3, 1, 0],
                [0, 3, 0],
                [0, 1, 1],
                [4, 3, 0]
            ]
        ]
        handle_line = [
            Line(
                my_vmobject.points[ind],
                my_vmobject.points[ind+1],
                color = BLUE,
                stroke_width = 2
            ) for ind in range(0, len(my_vmobject.points), 2)
        ]

        self.add(plane, *handles, *handle_line, my_vmobject)