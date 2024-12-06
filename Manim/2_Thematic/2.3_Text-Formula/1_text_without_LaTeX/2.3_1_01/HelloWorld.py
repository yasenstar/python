from manim import *

class HelloWorld(Scene):
    def construct(self):
        text1 = Text("Hello World", font_size=50).move_to(UP*2)
        text2 = Text("I like Manim", font_size=80, color = RED)
        self.add(text1, text2)