from turtle import Turtle


INITIAL_POSITION = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(INITIAL_POSITION)

    def move(self):
        self.forward(10)

    def go_starting_point(self):
        self.goto(INITIAL_POSITION)

    def end_of_line(self):
        if self.ycor() >= 290:
            #print(self.ycor())
            return True
        else:
            return False