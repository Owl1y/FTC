from manim import *

class GraphAreaPlot(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 5],
            y_range=[0, 6],
            x_axis_config={"numbers_to_include": [2, 3]},
            tips=False,
        )

        labels = ax.get_axis_labels()

        curve_1 = ax.get_graph(lambda x: 4 * x - x ** 2, x_range=[0, 4], color=BLUE_C)
        curve_2 = ax.get_graph(
            lambda x: 0.8 * x ** 2 - 3 * x + 4,
            x_range=[0, 4],
            color=GREEN_B,
        )

        line_1 = ax.get_vertical_line(ax.input_to_graph_point(2, curve_1), color=YELLOW)
        line_2 = ax.get_vertical_line(ax.i2gp(3, curve_1), color=YELLOW)

        area_1 = ax.get_area(curve_1, x_range=[0.3, 0.6], dx_scaling=40, color=BLUE)
        area_2 = ax.get_area(curve_2, [2, 3], bounded=curve_1, color=GREY, opacity=0.2)

        self.add(ax, labels, curve_1, curve_2, line_1, line_2, area_1, area_2)


class SineCurveUnitCircle(Scene):
    # contributed by heejin_park, https://infograph.tistory.com/230
    def construct(self):
        self.show_axis()
        #self.show_circle()
        self.move_dot_and_draw_curve()
        self.wait()

    def show_axis(self):
        x_start = np.array([-6,0,0])
        x_end = np.array([6,0,0])

        y_start = np.array([-4,-2,0])
        y_end = np.array([-4,2,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_x_labels()

        self.origin_point = np.array([-4,0,0])
        self.curve_start = np.array([-3,0,0])

    def add_x_labels(self):
        x_labels = [
            MathTex("a"), MathTex("2"),
            MathTex("1"), MathTex("b"),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)
            self.add(x_labels[i])

    def show_circle(self):
        circle = Circle(radius=1)
        circle.move_to(self.origin_point)
        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        origin_point = self.origin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)

        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )


        self.curve = VGroup()
        self.curve.add(Line(self.curve_start,self.curve_start))
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            self.curve.add(new_line)

            return self.curve

        dot.add_updater(go_around_circle)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        sine_curve_line = always_redraw(get_curve)

        self.add(dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
        self.wait(8.5)

        dot.remove_updater(go_around_circle)

class Shapes(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)
        circ2 = Circle()

        circ2.set_fill(PINK, opacity=0.5)
        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(TEAL, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.5)

       # self.add(circle, square, triangle)
        self.play(FadeIn(square, circle))
        self.play(ApplyMethod(circle.set_color, WHITE), run_time=0.5)
        self.play(ApplyMethod(circle.shift, UP), run_time=0.5)
        self.play(ApplyMethod(circle.shift, RIGHT), run_time=0.5)
        self.play(Transform(circle, circ2))
        self.play(Rotate(square, PI/4))
        self.play(Transform(circle, square))
        #self.play(FadeOut(circle))
        #self.play(FadeOut(square))

        self.wait(1)


class firstL(Scene):
    def construct(self):
       tex = Tex(r"x")
       self.add(tex.scale(8))

class secondL(Scene):
    def construct(self):
       tex = Tex(r"b")
       self.add(tex.scale(8))

class limit(Scene):
    def construct(self):
       tex = Tex(r"x+h")
       self.add(tex.scale(8))

class mathtexts(Scene):
    def construct(self):
       tex = Tex(r"x+h")
       tex1 = MathTex(r"A(x) = \int_{a}^{x}f(t) dt") 
       tex2 = MathTex(r"A'(x) = \lim_{h \to 0} \frac{A(x+h) - A(x)}{h}") 
       tex3 = MathTex(r"\lim_{h \to 0} \frac{\int_{a}^{x+h}f(t) dt - \int_{a}^{x}f(t)dt}{h}")
       tex4 = MathTex(r"\lim_{h \to 0} \int_{x}^{x+h}f(t) dt")
       tex5 = MathTex(r"\int_{a}^{x + h}f(t) dt - \int_{a}^{x}f(t) dt")
       tex6 = MathTex(r"f(x) * h") 
       tex7 = MathTex(r"\frac{f(x) * h}{h}")
       tex8 = MathTex(r"\lim_{h \to 0} \frac{f(x) * h}{h}")

       self.add(tex8.scale(2))


"""this is an integral animation i got from the manim discord"""
class empty_integral(Scene):
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
      
        self.play(Write(axes, lag_ratio = 0.01,run_time = 2))
        t=ValueTracker(50)

        interval = [0,8]
        function = lambda x : 0.011*(x+5)*((x-3)**2) + 2
        graph = axes.get_graph(function, color = BLUE)
        label = axes.get_graph_label(graph, "f(x)")


        self.play(Create(graph), lag_ratio = 0.01, run_time = 2)
        self.wait(3)
 








