from manim import *

class IterateColor(Scene):
    def construct(self):
        text = Text("A Lot Of Colors", font_size=96)
        for letter in text:
            letter.set_color(random_bright_color())
        self.add(text)