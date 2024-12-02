from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()
        
        square.flip(RIGHT)
        triangle.flip(DOWN)
        
        square.rotate(-3 * TAU / 8)
        
        circle.set_fill(PINK, opacity=0.5)
        triangle.set_fill(BLUE, opacity=0.7)
        
        self.play(Create(square))
        self.play(Transform(square, circle), run_time = 5)
        self.play(FadeOut(square))
        self.play(Transform(square, triangle), run_time = 5)
        self.play(FadeOut(square))
        self.wait()