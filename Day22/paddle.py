from turtle import Turtle

INITIAL_POSITIONS = [(-390, 0), (380, 0)]
MOVE_DISTANCE = 20


class Pad(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.speed("fastest")
        self.goto(pos)

    def up(self):
        xcor = self.xcor()
        ycor = self.ycor()
        self.goto(xcor, ycor + MOVE_DISTANCE)

    def down(self):
        xcor = self.xcor()
        ycor = self.ycor()
        self.goto(xcor, ycor - MOVE_DISTANCE)