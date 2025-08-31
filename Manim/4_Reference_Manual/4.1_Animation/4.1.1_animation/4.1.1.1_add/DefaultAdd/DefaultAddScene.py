from manim import *

class DefaultAddScene(Scene):
    def construct(self):
        text_1 = Text("I was added with Add!")
        text_2 = Text("Me too!")
        text_3 = Text("And Me!")
        texts = VGroup(text_1, text_2, text_3).arrange(DOWN)
        rect = SurroundingRectangle(texts, buff = 0.5)

        self.play(
            Create(rect, run_time = 4.0),
            Succession(
                Wait(2.0),
                Add(text_1),
                Wait(1.0),
                Add(text_2),
                Wait(1.0),
                Add(text_3)
            )
        )
        self.wait()