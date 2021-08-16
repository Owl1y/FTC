from manim import *
import numpy as np
import scipy.integrate as integrate




class FunctionPlotWithLabelledYAxis(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            y_min=0,
            y_max=100,
            y_axis_config={"tick_frequency": 10},
            y_labeled_nums=np.arange(0, 100, 10),
            **kwargs
        )

    def construct(self):
        self.setup_axes()
        dot = Dot().move_to(self.coords_to_point(PI / 2, 20))
        func_graph = self.get_graph(lambda x: 20 * np.sin(x))
        self.add(dot,func_graph)



class graph_f_sucks(Scene):
    def construct(self):

        backg_plane = NumberPlane(x_range=[0,10,1], y_range=[0,10,1])
        graph_of_f = Axes(
            x_range = [0, 10, 1], y_range = [0, 100, 1],
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
        t=ValueTracker(0)

        axis_labels = graph_of_f.get_axis_labels("x", "y")

        graph = graph_of_f.get_graph(lambda x: x**2, x_range = [0,10], color = BLUE)
        graphing_stuff = VGroup(graph_of_f, graph, axis_labels, black_box).scale(0.5)
        line1 = always_redraw(lambda:graph_of_f.get_vertical_line(graph_of_f.i2gp(t.get_value(), graph), color=YELLOW))

        self.play(FadeIn(black_box, target_position=graph_of_f))
        #LEFT*2.3 + DOWN*2.7
        self.play(black_box.animate.shift(LEFT*2.3 + DOWN*2.5).scale(0.3), run_time=3)
        self.play(DrawBorderThenFill(graph_of_f), Write(axis_labels), run_time= 2)
        self.wait()
        self.play(Create(graph),black_box.animate.shift(RIGHT*4.6), run_time = 2)
        self.play(Write(line1))
        self.wait()



"""this is an integral animation i got from the manim discord"""
class integral(Scene):

    def construct(self):
        axes = Axes(
            x_range=[0,8],
            y_range=[0,7],
            axis_config = {
                "color": WHITE,
                "include_ticks": False
                },
                #x_axis_config={"numbers_to_include": [4, 6]},
                tips = False)

        #self.add(axes.add_coordinates())

        self.play(Write(axes, lag_ratio = 0.01,run_time = 2))
        t=ValueTracker(50)

        interval = [0,8]
        function = lambda x : 0.011*(x+5)*((x-3)**2) + 2
        graph = axes.get_graph(function, color = BLUE)
        label = axes.get_graph_label(graph, "f(x)")


        self.play(Create(graph),FadeIn(label), lag_ratio = 0.01, run_time = 2)
        #line1 =  always_redraw(lambda:axes.get_vertical_line(axes.i2gp(t.get_value(), graph), color=YELLOW))

        rects = axes.get_area(graph,interval,dx_scaling=30)
        rects.add_updater(lambda x: x.become(axes.get_area(graph, interval ,dx_scaling=t.get_value())))
        self.play(Create(rects),run_time = 2)
        self.play(t.animate(run_time=4,rate_func=linear).set_value(1))
        #self.add(add_x_labels)
        answer = self.intg(4,6)

        #self.play(Write(Tex(answer)))
        self.wait(2)
    def intg(self,a, b):

        func = lambda x : 0.011*(x+5)*((x-3)**2) + 2
        return (integrate.quad(func,a,b))[0]


class Secintegral(Scene):
    def construct(self):



