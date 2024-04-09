from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position,color) :
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.speed('fastest')
        self.color(color)
        self.penup()
        self.goto(position)
   
    def move_up(self):
        if self.ycor()< 240:
         new_y=self.ycor()+30
         self.goto(self.xcor(),new_y)

    def move_down(self):
        if self.ycor()> -240:
         new_y=self.ycor()-30
         self.goto(self.xcor(),new_y)
