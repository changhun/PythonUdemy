import turtle as t

INIT_POSITIONS = [(0, 0,), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        for i in range(len(INIT_POSITIONS)):
            new_turtle = t.Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(INIT_POSITIONS[i])

            self.segments.append(new_turtle)

    def move(self):
        print(f"moving. xcor: {self.segments[0].xcor()} ycor: {self.segments[0].ycor()}")
        for i in range(len(self.segments) - 1, 0, -1):
            xcor = self.segments[i-1].xcor()
            ycor = self.segments[i-1].ycor()
            self.segments[i].goto(xcor, ycor)
        self.segments[0].forward(20)

    def turn_left(self):
        heading = self.segments[0].heading()
        self.segments[0].setheading(heading+90)

    def turn_right(self):
        heading = self.segments[0].heading()
        self.segments[0].setheading(heading - 90)

    def feed(self):
        xcor = 2* self.segments[-1].xcor() - self.segments[-2].xcor()
        ycor = 2* self.segments[-1].ycor() - self.segments[-2].ycor()
        new_turtle = t.Turtle()
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(xcor, ycor)
        new_turtle.shape("square")
        self.segments.append(new_turtle)