from manim import *

class GradientImageFromArray(Scene):
    def construct(self):
        n = 256
        imageArray = np.uint8(
            [
                [i * 256 / n for i in range(0, n)]
                for _ in range(0, n)
            ]
        )
        image = ImageMobject(imageArray).scale(3)
        image.background_rectangle = SurroundingRectangle(image, BLUE, fill_opacity=0)
        self.add(image.background_rectangle, image)