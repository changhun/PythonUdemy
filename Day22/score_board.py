from turtle import Turtle


ALIGN = "left"
FONT = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("blue")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def score_up(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def show(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)