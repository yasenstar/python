from manim import *

class AddPackageLaTeX(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        tex1 = Tex(
            r"$\mathscr{H} \rightarrow \mathbb{H}$",
            tex_template=myTemplate,
            color = RED,
            font_size=144
        )
        tex2 = MathTex(
            r"\mathscr{H} \rightarrow \mathbb{H}",
            tex_template=myTemplate,
            color = GREEN,
            font_size=144
        )
        self.add(VGroup(tex1,tex2).arrange(DOWN))