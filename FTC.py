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
        graph_of_dt.add_coordinates()fil



        #graph_of_dt.to_edge(UR)
        axis_labels = graph_of_dt.get_axis_labels("time", "distance")


        graph = graph_of_dt.get_graph(lambda x: x**0.6, x_range = [0,10], color = BLUE)
        graphing_stuff = VGroup(graph_of_dt, graph, axis_labels).scale(0.5)


        self.play(DrawBorderThenFill(graph_of_dt), Write(axis_labels), run_time= 2)
        self.wait()
        self.play(Create(graph), run_time = 2)

#this shows how ass the function f(x) is and is way to abstract 
class graph_f_sucks(Scene):
    def construct(self):

        backg_plane = NumberPlane(x_range=[0,10,1], y_range=[0,10,1])
        graph_of_f = Axes(
            x_range = [0, 10, 1],
            y_range = [0, 100, 1],
            x_length = 10,
            y_length = 10,
            axis_config = {
                "color": WHITE,
                "include_ticks": False,
                },
            x_axis_config={
                #"numbers_to_include": np.arange(0, 10.01, 2),
                #"numbers_with_elongated_ticks": np.arange(0, 10.01, 2),
            },
            tips = False)

        square = Square()
        fx = MathTex("f(x)")
        black_box = VGroup(square, fx)


        axis_labels = graph_of_f.get_axis_labels("x", "y")

        graph = graph_of_f.get_graph(lambda x: x**2, x_range = [0,10], color = BLUE)
        graphing_stuff = VGroup(graph_of_f, graph, axis_labels, black_box).scale(0.5)

        self.play(FadeIn(black_box, target_position=graph_of_f))
        #LEFT*2.3 + DOWN*2.7
        self.play(black_box.animate.shift(LEFT*2.3 + DOWN*2.5).scale(0.3), run_time=3)
        self.play(DrawBorderThenFill(graph_of_f), Write(axis_labels), run_time= 2)
        self.wait()
        self.play(Create(graph),black_box.animate.shift(RIGHT*4.6), run_time = 2)
        self.wait()
