from manim import *

class SingleLineColor(Scene):
    def construct(self):
        text = MarkupText(
            f'all in read <span fgcolor="{YELLOW}">except this</span>',
            color = PURPLE
        )
        self.add(text)