from manim import *

class LineSpacing(Scene):
    def construct(self):
        t1 = Text("Hello\nWorld", line_spacing=1, color=RED)
        t2 = Text("Hello\nWorld", line_spacing=2)
        # self.add(Group(t1,t2))
        self.add(Group(t1,t2).arrange(LEFT, buff=1.5))