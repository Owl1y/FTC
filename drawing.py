from manim import *


class Sample(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        vectorlogo = "3B1B"
        drawingPic = SVGMobject(vectorlogo)
        drawingPic.scale(2)
        self.play(DrawBorderThenFill(drawingPic))
        self.wait(1)
