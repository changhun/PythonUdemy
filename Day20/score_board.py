from turtle import Turtle

ALIGN = 'left'
FONT = ('Arial', 15, 'normal')
FONT2 = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-40, 290)
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def increasing(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(-60, 0)
        self.write("Game Over", align=ALIGN, font=FONT2)