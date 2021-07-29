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
        self.play(FadeOut(gx), run_time = 0.5)
        self.wait(2)


#The graph d(t)
class graphd(Scene):
    def construct(self):
        backg_plane = NumberPlane(x_range=[0,10,1], y_range=[0,10,1]).add_coordinates()
        graph_of_dt = Axes(
            x_range = [0, 10, 1],
            y_range = [0, 10, 1],
            x_length = 10,
            y_length = 10,
            axis_config = {
                "color": WHITE,
                },
            x_axis_config={
                "numbers_to_include": np.arange(0, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(0, 10.01, 2),
            },
            tips=False)
        graph_of_dt.add_coordinates()



        #graph_of_dt.to_edge(UR)
        axis_labels = graph_of_dt.get_axis_labels("time", "distance")


        graph = graph_of_dt.get_graph(lambda x: x**0.6, x_range = [0,10], color = BLUE)
        graphing_stuff = VGroup(graph_of_dt, graph, axis_labels).scale(0.5)


        self.play(DrawBorderThenFill(graph_of_dt), Write(axis_labels), run_time= 2)
        self.wait()
        self.play(Create(graph), run_time = 2)
