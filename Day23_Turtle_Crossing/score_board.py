from turtle import Turtle

INITIAL_POSITION = (-50, 260)
FONT = ('Arial', 12, 'normal')
FONT_GAME_OVER = FONT = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(INITIAL_POSITION)
        self.write(f"level{self.level}", align='left', font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"level{self.level}", align='left', font=FONT)

    def game_over(self):
        self.goto(-50, 0)
        self.write(f"Game Over", align='left', font=FONT_GAME_OVER)
