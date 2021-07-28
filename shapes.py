from manim import *

class Shapes(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(TEAL, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.5)

       # self.add(circle, square, triangle)
        self.play(FadeIn(square, circle))
        self.play(ApplyMethod(circle.set_color, WHITE), run_time=0.5)
        self.play(ApplyMethod(circle.shift, UP), run_time=0.5)
        self.play(ApplyMethod(circle.shift, RIGHT), run_time=0.5)
        self.play(Rotate(square, PI/4))
        self.play(Transform(circle, square))
        #self.play(FadeOut(circle))
        #self.play(FadeOut(square))
        
        self.wait(1)

class MobjectExample(Scene):
    def construct(self):
        p1= [-1,-1,0]
        p2= [1,-1,0]
        p3= [1,1,0]
        p4= [-1,1,0]
        a = Line(p1,p2).append_points(Line(p2,p3).get_points()).append_points(Line(p3,p4).get_points())
        point_start= a.get_start()
        point_end  = a.get_end()
        point_center = a.get_center()
        self.add(Text(f"a.get_start() = {np.round(point_start,2).tolist()}").scale(0.5).to_edge(UR).set_color(YELLOW))
        self.add(Text(f"a.get_end() = {np.round(point_end,2).tolist()}").scale(0.5).next_to(self.mobjects[-1],DOWN).set_color(RED))
        self.add(Text(f"a.get_center() = {np.round(point_center,2).tolist()}").scale(0.5).next_to(self.mobjects[-1],DOWN).set_color(BLUE))

        self.add(Dot(a.get_start()).set_color(YELLOW).scale(2))
        self.add(Dot(a.get_end()).set_color(RED).scale(2))
        self.add(Dot(a.get_top()).set_color(GREEN_A).scale(2))
        self.add(Dot(a.get_bottom()).set_color(GREEN_D).scale(2))
        self.add(Dot(a.get_center()).set_color(BLUE).scale(2))
        self.add(Dot(a.point_from_proportion(0.5)).set_color(ORANGE).scale(2))
        self.add(*[Dot(x) for x in a.get_points()])
        self.add(a) 

class function(Scene):
    def construct(self):
        fx = Tex(r"f(x)").scale(4)
        gx = Tex(r"\xcancel{f(x)}") 
        self.play(FadeIn(fx))
        self.wait(1)
        self.play(FadeOut(fx))
