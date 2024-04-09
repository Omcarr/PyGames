from turtle import Turtle
FONT=('Courier', 20, 'bold')
ALIGNMENT ='center'
class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score_update(1)

    # board setup
    def board(self):
        self.hideturtle()
        self.color('white')
        self.penup()
        self.speed('fastest')

    def score_update(self,level):
        self.board()
        self.clear()
        self.goto(-330,270)
        self.write(f'Level:{level}', align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.board()
        self.goto(0,0)
        self.write(f'GAME OVER!', align=ALIGNMENT, font=FONT)
        

    