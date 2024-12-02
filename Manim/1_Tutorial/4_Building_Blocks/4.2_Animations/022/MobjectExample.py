from manim import *

class MobjectExample(Scene):
    def construct(self):
        p1 = [-1, -1, 0]
        p2 = [1, -1, 0]
        p3 = [1, 1, 0]
        p4 = [-1, 1, 0]

        a = Line(p1,p2)
        a.append_points(Line(p2,p3).points)
        a.append_points(Line(p3,p4).points)

        point_start = a.get_start()
        point_end = a.get_end()
        point_center = a.get_center()

        self.add(a)
        self.add(Text(f"a.get_start() = {np.round(point_start,2).tolist()}", font_size=24).to_edge(UR).set_color(YELLOW))
        self.add(Text(f"a.get_end() = {np.round(point_start,2).tolist()}", font_size=24).next_to(self.mobjects[-1],DOWN).set_color(RED))
        self.add(Text(f"a.get_center() = {np.round(point_start,2).tolist()}", font_size=24).next_to(self.mobjects[-1],DOWN).set_color(BLUE))

        self.add(Dot(a.get_start()).set_color(YELLOW).scale(5))
        self.add(Dot(a.get_end()).set_color(RED).scale(5))
        self.add(Dot(a.get_top()).set_color(GREEN_A).scale(5))
        self.add(Dot(a.get_bottom()).set_color(PURE_GREEN).scale(5))
        self.add(Dot(a.get_center()).set_color(PURE_BLUE).scale(5))
        self.add(Dot(a.point_from_proportion(0.6)).set_color(ORANGE).scale(5))

        self.add(*[Dot(x).set_color(LIGHT_PINK) for x in a.points])