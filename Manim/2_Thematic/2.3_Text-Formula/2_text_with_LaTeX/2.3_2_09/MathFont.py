from manim import *

class LaTeXMathFonts(Scene):
    def construct(self):
        tex1 = Tex(
            r"$x^2 + y^2 = z^2$",
            tex_template = TexFontTemplates.french_cursive,
            font_size = 144
        )
        tex2 = Tex(
            r"$x^3 - y^3 = z^3$",
            tex_template = TexFontTemplates.latin_modern_tw_it,
            font_size = 144
        )
        self.add(VGroup(tex1,tex2).arrange(DOWN))