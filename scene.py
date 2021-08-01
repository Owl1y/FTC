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


class GRAPH(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes= Axes(x_range=[-4,4],
            y_range=[-4,16,2],
            axis_config={"color":BLACK},
            y_length=7,
            x_axis_config={
                "numbers_to_include": np.arange(-4,4.1,1)
            }
        )

        ax_labels = axes.get_axis_labels(x_label="x",y_label="g(x)" )
        def func(x):
            return x/(x**2+x) # The rational function.
        graph = axes.get_graph(func, color=RED, use_smoothing=False, discontinuities=[-1, 0, 0])

        text=MathTex("g(x)=\\frac{x}{x^2+x}")
        text.shift(5 * RIGHT + 0.5 * UP)

        self.add(axes,ax_labels,graph)
        self.add(ax_labels.set_color(BLACK))
        self.add(text.set_color(TEAL))
