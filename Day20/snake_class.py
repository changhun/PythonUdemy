import turtle as t

INIT_POSITIONS = [(0, 0,), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in INIT_POSITIONS:
            new_turtle = t.Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(position)
            self.segments.append(new_turtle)

    def move(self):
        print(f"moving. xcor: {self.head.xcor()} ycor: {self.head.ycor()}")
        for i in range(len(self.segments) - 1, 0, -1):
            xcor = self.segments[i-1].xcor()
            ycor = self.segments[i-1].ycor()
            self.segments[i].goto(xcor, ycor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def feed(self):
        xcor = 2* self.segments[-1].xcor() - self.segments[-2].xcor()
        ycor = 2* self.segments[-1].ycor() - self.segments[-2].ycor()
        new_turtle = t.Turtle()
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(xcor, ycor)
        new_turtle.shape("square")
        self.segments.append(new_turtle)