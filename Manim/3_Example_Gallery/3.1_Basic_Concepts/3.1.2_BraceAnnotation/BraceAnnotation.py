from manim import *

class BraceAnnotation(Scene):
    def construct(self):

        # Draw Line
        dot1 = Dot([-2, -1, 0]).set_color(BLUE)
        dot2 = Dot([2, 1, 0]).set_color(GREEN)
        line = Line(dot1.get_center(), dot2.get_center()).set_color(ORANGE)

        # Horizontal brace annotation
        b1 = Brace(line)
        b1text = b1.get_text("Horizontal Distance")

        b2 = Brace(line, direction=line.copy().rotate(PI/2).get_unit_vector())
        b2text = b2.get_tex("x-x_1")

        # Add into Scene
        self.add(dot1, dot2, line, b1, b1text, b2, b2text)