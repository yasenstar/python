from manim import *

class LaTeXCommands(Scene):
    def construct(self):
        tex1 = Tex(r'$\mathtt{H} \looparrowright \mathtt{H} \looparrowleft$ \LaTeX', font_size=144)
        tex2 = MathTex(r'\mathtt{H} \looparrowright \mathtt{H} \looparrowleft', font_size=144)

        tex3 = Tex(r"Hello \LaTeX", color=BLUE, font_size=144)
        tex4 = MathTex(r"\mathtt{H} \looparrowleft", color=BLUE, font_size=144)

        self.add(VGroup(tex1, tex2, tex3, tex4).arrange(DOWN))