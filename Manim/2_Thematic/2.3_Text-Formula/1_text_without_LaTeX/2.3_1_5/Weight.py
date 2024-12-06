from manim import *

class DifferentWeight(Scene):
    def construct(self):
        import manimpango
        g = VGroup()
        weight_list = dict(
            sorted(
                {
                    weight: manimpango.Weight(weight).value
                    for weight in manimpango.Weight
                }.items(),
                key = lambda x: x[1],
            )
        )
        for weight in weight_list:
            g += Text(weight.name, weight=weight.name, font="Impact")
        
        self.add(g.arrange(DOWN).scale(0.5))