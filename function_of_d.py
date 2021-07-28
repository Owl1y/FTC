from manim import *
import numpy as np
import random

class graphd(GraphScene):
  
    graph_of_dt = Axes{
        "x_min": 0,
        "x_max": 10,
        "y_min": 0,
        "y_max": 10,
        "x_axis_label": r"time",
        "y_axis_label": r"distance"
    } 
    
   

    def show_function_graph(self):
        self.setup_axes(animate=True)

        func = lambda x: x**2
        
        graph = self.get_graph(func, x_min=0, x_max=10)
        self.play(Create(graph))

    def construct(self):
        self.show_function_graph()