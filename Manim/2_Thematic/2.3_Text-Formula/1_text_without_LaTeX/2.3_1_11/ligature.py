from manim import *

class DisableLigatures(Scene):
    def construct(self):
        li = Text("fl ligature", disable_ligatures=False, font_size=70)
        nli = Text("fl ligature", disable_ligatures=True, font_size=70)
        li2 = Text("fl ligature", disable_ligatures=False, font_size=96)
        nli2 = Text("fl ligature", disable_ligatures=True, font_size=96)
        self.add(Group(li, nli, li2, nli2).arrange(DOWN, buff=0.5))