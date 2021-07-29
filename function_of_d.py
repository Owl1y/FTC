from manim import *
import numpy as np
import random

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

        #self.play(FadeIn(backg_plane), run_time=6)
        #self.play(backg_plane.animate.set_opacity(0.3))
        #self.wait()
        self.play(DrawBorderThenFill(graph_of_dt), Write(axis_labels), run_time= 2)
        self.wait()
        self.play(Create(graph), run_time = 2)
        """self.play(graphing_stuff.animate.shift(DOWN*4), run_time = 3)
        self.wait()
        self.play(graph_of_dt.animate.shift(LEFT*3), run_time = 3)
        self.wait()"""


"""class Exercice12(Scene):
    def construct(self):
        self.plane = NumberPlane(x_range=[-1, 6], y_range=[-3, 5]).scale(0.7)
        x, x_label = self.get_vectors()[0], self.get_vectors()[1]
        y, y_label = self.get_vectors()[2], self.get_vectors()[3]
        self.add(self.plane, self.get_vectors())

    def get_vectors(self):
        x = Arrow(self.plane.c2p(0, 0), self.plane.c2p(4, 2), color=YELLOW,buff=0)
        x_label = MathTex('x').next_to(x, DOWN)
        y = Arrow(self.plane.c2p(0, 0), self.plane.c2p(3, 4), color=YELLOW,buff=0)
        y_label = MathTex('y').next_to(y, UP)
        return VGroup(x, x_label, y, y_label)"""
