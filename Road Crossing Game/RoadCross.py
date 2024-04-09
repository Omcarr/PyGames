from turtle import Screen
import time
from RoadCross_Cars import Cars
from RoadCross_Player import Tortoise
from RoadCross_Score import Board

#game variables
LEVEL=1
SPEED=0.25
game_is_on=True

#setup of the Screen
my_screen=Screen()
my_screen.setup(800,600)
my_screen.bgcolor('black')
my_screen.title('RoadRash')
my_screen.tracer(0)

car=Cars()
tim=Tortoise()
board=Board()

my_screen.listen()
my_screen.onkey(tim.move_up,'Up')

while game_is_on:
    my_screen.update()
    time.sleep(SPEED)
    car.create_car()
    car.car_move()

    #level cleared
    if tim.ycor()> 270:
        LEVEL+=1
        SPEED*=0.9
        board.score_update(LEVEL)
        time.sleep(0.2)
        tim.goto(0,-275)

    #turtle hit a car, game over
    for new_car in car.ALL_CARS:
     if tim.distance(new_car)<20:
        board.game_over()
        car.stop_cars()
        time.sleep(3)
        print('\nThank you for playing!!')
        print(f'You cleared upto Level: {LEVEL-1}\n')
        exit()

