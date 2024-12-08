from manim import *

class IndexLabelsMathTex(Scene):
    def construct(self):
        text1 = MathTex(r"\binom{2n}{n+2}", font_size=96)
        text2 = MathTex(r"\dbinom{2n-m}{n+2}", font_size=96)

        self.add(index_labels(text1[0]))
        self.add(index_labels(text2[0]))

        text1[0][1:3].set_color(YELLOW)
        text2[0][4:7].set_color(GREEN)

        self.add(VGroup(text1, text2).arrange(DOWN))