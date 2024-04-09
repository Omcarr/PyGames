import time
from turtle import Screen
from PinPong_paddle import Paddle
from PinPong_Ball import Ball
from PinPong_Scoreboard import ScoreBoard as board

game_is_on = True

my_screen = Screen()
my_screen.bgcolor('black')
my_screen.title('The Pin-Pong Game')
my_screen.setup(800, 600)
my_screen.tracer(0)
left_paddle = Paddle((-380, 0),'red')
right_paddle = Paddle((380, 0),'blue')

ball = Ball()
board = board()

# controller
my_screen.listen()
my_screen.onkeypress(left_paddle.move_up, 'w')
my_screen.onkeypress(left_paddle.move_down, 's')
my_screen.onkeypress(right_paddle.move_up, 'Up')
my_screen.onkeypress(right_paddle.move_down, 'Down')

while game_is_on:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.ball_move()

# detect the wall colliosion with top & bottom walls & bounces
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.Bounce_Vertical()

   # paddle hits
    if (ball.distance(left_paddle) < 50 and ball.xcor() < -350):
        ball.Bounce_Horizontal()
    elif (ball.distance(right_paddle) < 50 and ball.xcor() > 350):
        ball.Bounce_Horizontal()
   
    # Point for blue player
    if ball.xcor() < -370:
        board.Score_Right += 1
        
        ball.reset()
        board.board(board.Score_left, board.Score_Right)

    # point for red player
    elif ball.xcor() > 370:
        board.Score_left += 1
        ball.reset()
        board.board(board.Score_left, board.Score_Right)
    
    #Game over
    if board.Score_Right==5:
       time.sleep(2)
       board.win_condition(color='blue')
       time.sleep(5)
       game_is_on=False

    elif board.Score_left==2:
         time.sleep(2)
         board.win_condition(color='red')
         time.sleep(5)
         game_is_on=False