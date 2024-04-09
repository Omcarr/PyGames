from turtle import Turtle

FONT=('Courier', 40, 'bold')
ALIGNMENT ='center'

class ScoreBoard(Turtle):
     Score_left=0
     Score_Right=0

     def __init__(self):
          super().__init__()
          self.board(self.Score_left,self.Score_Right)

     def win_condition(self,color):
          self.speed('fastest')
          self.goto(0,0)
          self.penup()
          self.hideturtle()
          self.color(color)
          self.write(f'{color.upper()} WON!', align=ALIGNMENT, font=FONT)

     def board(self,left,right):
          self.clear()
          self.penup()
          self.hideturtle()
          self.color('white')
          self.speed('fastest')
          self.goto(-200,240)
          self.write(f'{left}', align=ALIGNMENT, font=FONT)
          self.goto(200,240)
          self.write(f'{right}', align=ALIGNMENT, font=FONT)



