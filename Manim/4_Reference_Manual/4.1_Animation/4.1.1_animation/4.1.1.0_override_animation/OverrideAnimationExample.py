from manim import *

class MySquare(Square):
    @override_animation(FadeIn)
    def _fade_in_override(self, **kwargs):
        return Create(self, **kwargs)

class OverrideAnimationExample(Scene):
    def construct(self):
        # built-in function
        # square = Create(Square())
        # self.play(square)
        self.play(FadeIn(MySquare()))