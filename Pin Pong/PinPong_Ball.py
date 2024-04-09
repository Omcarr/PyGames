from turtle import Turtle


class Ball(Turtle):
    def __init__(self,):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.clear()
        self.shape('circle')
        self.speed('fastest')
        self.color('white')
        self.penup()
        self.goto(0,0)
        self.X_val=20
        self.Y_val=20
        self.move_speed=0.1

    def ball_move(self):
        X=self.xcor()+self.X_val
        Y=self.ycor()+self.Y_val
        self.goto(X,Y)

    def Bounce_Vertical(self):
        self.Y_val*= -1
        self.move_speed*=0.95
    
    def Bounce_Horizontal(self):
        self.X_val*= -1
    
    def reset(self):
        self.goto(0,0)
        self.Bounce_Horizontal()