from manim import *

class GradientExample(Scene):
    def construct(self):
        t1 = Text("Hello", gradient=(RED, BLUE, GREEN), font_size=68)
        t2 = Text("Hello", gradient=(RED, BLUE, GREEN), font_size=69)
        t3 = Text("Hello", gradient=(RED, BLUE, GREEN), font_size=70)
        t4 = Text("Hello", gradient=(RED, BLUE, GREEN), font_size=71)
        t5 = Text("Hello", gradient=(RED, BLUE, GREEN), font_size=72)

        self.add(Group(t1,t2,t3,t4,t5).arrange(DOWN))