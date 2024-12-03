from manim import *

class ShowScreenResolution(Scene):
    def construct(self):
        pixel_height = config["pixel_height"]
        pixel_width = config["pixel_width"]
        frame_width = config["frame_width"]
        frame_height = config["frame_height"]

        self.add(Dot())

        d1 = Line(frame_width * LEFT / 2, frame_width * RIGHT / 2).to_edge(DOWN)
        self.add(d1)

        self.add(Text(str(pixel_width)).next_to(d1,UP))

        d2 = Line(frame_height * UP / 2, frame_height * DOWN / 2).to_edge(RIGHT)
        self.add(d2)

        self.add(Text(str(pixel_height)).next_to(d2,LEFT))
