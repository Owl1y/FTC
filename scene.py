from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(BLUE, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class SquareToCircleRed(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(RED, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen