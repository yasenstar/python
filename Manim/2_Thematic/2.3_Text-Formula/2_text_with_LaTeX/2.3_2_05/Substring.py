from manim import *

class LaTeXSubstrings(Scene):
    def construct(self):
        tex = Tex("Hello", r'$\bigstar$', r'LaTeX', r'$\frac{a}{b}$', font_size=120)
        tex.set_color_by_tex('igsta', BLUE)
        tex[0].set_color(RED)
        tex[3].set_color(YELLOW)
        tex.set_color_by_tex('TeX', GREEN)
        self.add(tex)