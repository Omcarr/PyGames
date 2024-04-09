from turtle import Turtle

class Tortoise(Turtle):
    # creates a turtlr at the bottom of the screen
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.shapesize(1.5,1.5)
        self.penup()
        self.setheading(90)
        self.goto(0,-275)

    #turtle is only allowed to move upwards
    def move_up(self):
        if self.ycor()< 275:
         Y_cor=self.ycor()+15
         X_cor=self.xcor()
         self.goto(X_cor,Y_cor)