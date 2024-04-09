from turtle import Turtle
import random

COLORS=["red", "green", "yellow",'Coral','blue','silver',
 "cyan", "orange", "pink","teal", "gold"]

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.ALL_CARS=[]

    #creats a car randomly at the right hand side end of the screen
    def create_car(self):
        #creats a car for approx 1 in 3 while loop iteration
        dice=random.randint(1,2)
        if dice==1:
         new_car=Turtle('square')
         new_car.speed('fastest')
         new_car.color(random.choice(COLORS))
         new_car.penup()
         new_car.shapesize(stretch_len=2,stretch_wid=1)
         # a new car created, goes to random location
         random_y=random.randint(-12,13)*20
         new_car.goto(290,random_y)
         self.ALL_CARS.append(new_car)
    
    #car keeps moving forward to the left end in x direction only
    def car_move(self):
        for car in self.ALL_CARS:
         x_cord=car.xcor()-20
         y_cord=car.ycor()
         car.goto(x_cord,y_cord)
    
    def stop_cars(self):
        for car in self.ALL_CARS:
            car.clear()

    