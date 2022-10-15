import turtle as t
import time

screen = t.Screen()
screen.screensize(canvwidth=600, canvheight=600)
screen.bgcolor("black")
screen.title("Snake Game")

positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for i in range(len(positions)):
    new_turtle = t.Turtle()
    new_turtle.penup()
    new_turtle.setpos(positions[i])
    new_turtle.color("white")
    new_turtle.shape("square")
    segments.append(new_turtle)

# print(f"screen.tracer: {screen.tracer()}")
screen.tracer(0)


def move():
    for i in range(len(segments)-1, 0, -1):
        turtle = segments[i]
        prev = segments[i-1]
        turtle.setpos(prev.position())

    segments[0].forward(20)
    screen.update()


#def turn_left(head):
def turn_left():
    heading = segments[0].heading()
    segments[0].setheading(heading + 90)


def turn_right():
    heading = segments[0].heading()
    segments[0].setheading(heading - 90)


screen.listen()
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")

while segments[0].xcor() < 300:
    # screen.delay(10)
    time.sleep(0.3)
    move()

screen.exitonclick()
