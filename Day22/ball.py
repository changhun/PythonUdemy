from turtle import Turtle


MOVE_DISTANCE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(-40)
        self.ball_speed = 0.05

    def move(self):
        self.forward(MOVE_DISTANCE)
        # print("Ball moving")

    def bounce_y(self):
        self.setheading(-self.heading())

    def bounce_x(self):
        heading = self.heading()
        # print(f"Collision with paddle. heading: {heading}")
        # print(f"xcor: {self.xcor()} ycor: {self.ycor()}")
        if heading > 0:
            heading = 180 - heading
        else:
            heading = -180 - heading
        self.setheading(heading)
        self.ball_speed *= 0.8

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.ball_speed = 0.05
