from turtle import Turtle


MOVE_DISTANCE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(-40)

    def move(self):
        self.forward(MOVE_DISTANCE)
        # print("Ball moving")

    def bounce(self):
        self.setheading(-self.heading())

    def bounce_collision(self):
        heading = self.heading()
        print(f"Collision with paddle. heading: {heading}")
        print(f"xcor: {self.xcor()} ycor: {self.ycor()}")
        if heading > 0:
            heading = 180 - heading
        else:
            heading = -180 - heading
        self.setheading(heading)

