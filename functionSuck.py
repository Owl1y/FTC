from manim import *
import numpy as np
import random


#intro to the FTC video
class function(Scene):
    def construct(self):
        fx = Tex(r"f(x)").scale(4)
        gx = Tex(r"lets use d(t)").scale(2)
        worst = Tex(r"worst example of a function")
        self.play(Transform(fx, worst), run_time = 3)
        self.wait(2)
        self.play(FadeOut(fx,worst))
        self.wait()
        self.play(FadeIn(gx))
        self.play(Rotating(gx), run_time = 1)
        self.play(FadeOut(gx), run_time = 0.5)
        self.wait(2)

class Graphss(Scene):
    def construct(self):
        axes = Axes(x_range=[-3,8],y_range=[-1,5])
        self.add(axes.add_coordinates())

        self.play(Write(axes, lag_ratio = 0.01,run_time = 1))
        t=ValueTracker(50)
        graph = axes.get_graph(lambda x : np.abs(x)*np.cos(x)*np.sin(x), color = BLUE)
        label = axes.get_graph_label(graph, "\\mid x \\mid cos(x)sin(x)")

        self.play(Create(graph),FadeIn(label), lag_ratio = 0.01, run_time = 2)

        rects = axes.get_area(graph,[2,4],dx_scaling=30)
        rects.add_updater(lambda x: x.become(axes.get_area(graph,[2,4],dx_scaling=t.get_value())))
        self.play(Create(rects),run_time = 2)
        self.play(t.animate(run_time=4,rate_func=linear).set_value(1))
        self.wait(2)



class LineGraphExample(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range = (0, 7),
            y_range = (0, 5),
            x_length = 7,
            axis_config={"include_numbers": True},
        )
        plane.center()
        line_graph = plane.get_line_graph(
            x_values = [0, 1.5, 2, 2.8, 4, 6.25],
            y_values = [1, 3, 2.25, 4, 2.5, 1.75],
            line_color=GOLD_E,
            vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
            stroke_width = 4,
        )
        self.add(plane, line_graph)
