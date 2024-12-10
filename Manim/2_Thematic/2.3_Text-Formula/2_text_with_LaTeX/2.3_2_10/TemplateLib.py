from manim import *

# class LaTeXTemplateLibrary(Scene):
#     def construct(self):
        # tex = Tex(
        #     r"{你好}",
        #     tex_template=TexTemplateLibrary.ctex,
        #     font_size = 96
        #     # font = "simhei"
        # )
        # self.add(tex)
class demo(Scene):
    def construct(self):
        t1 = MathTex(r"\text{你好}", tex_template=TexTemplateLibrary.ctex)
        self.play(Write(t1))
        t2 = Tex(r"你好", tex_template=TexTemplateLibrary.ctex)
        self.play(Write(t2).set_color(RED).next_to(t1,DOWN))
        self.wait()