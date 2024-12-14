from manim import *

class VectorArrow(Scene):
    def construct(self):
        numberplane = NumberPlane()

        dot = Dot(ORIGIN)
        dot_text = Text('(0,0)').next_to(dot,DOWN)

        arrow1 = Arrow(ORIGIN, [2,2,0], buff=0)
        arrow1_text = Text('(2,2)').next_to(arrow1.get_end(), LEFT)

        arrow2 = Arrow([2,2,0], [3,-2,0], buff=0)
        arrow2_text1 = Text('(2,2)').next_to(arrow2.get_start(), RIGHT)
        arrow2_text2 = Text('(3,-2)').next_to(arrow2.get_end(), RIGHT)

        self.add(numberplane, dot, dot_text, arrow1, arrow1_text, arrow2, arrow2_text1, arrow2_text2)

# One question: shall we get middle-point from one arrow line?