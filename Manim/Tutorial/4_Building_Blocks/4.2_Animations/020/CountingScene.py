from manim import *

class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        super().__init__(number, **kwargs)
        self.start = start
        self.end = end
    
    def interpolate_mobject(self, alpha: float) -> None:
        value = self.start + (alpha * (self.end - self.start))
        self.mboject.set_value(value)

class CountingScene(Scene):
    def construct(self):
        number = DecimalNumber()
        
        number.add_updater(lambda number: number.move_to(ORIGIN))

        self.add(number)

        self.wait()

        self.play(Count(number, 0, 100), run_time = 4, rate_func = linear)

        self.wait()