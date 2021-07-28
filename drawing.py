class Sample(Scene):
    def construct(self):
        vectorlogo = "/home/a/Documents/cojects/FTC/Vector_Logos.svg"  
        drawingPic = SVGMobject("./Vector_Logos.svg") 
        drawingPic.scale(2)
        self.play(FadeIn(drawingPic))
        self.wait(4)


