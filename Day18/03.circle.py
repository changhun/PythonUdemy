import turtle as t
import random

t.colormode(255)


def random_color():
    r = random.choice(range(0, 255))
    g = random.choice(range(0, 255))
    b = random.choice(range(0, 255))
    rgb = (r, g, b)
    return rgb


def draw_circle(num):
    angle = 360 / num

    for i in range(0, num):
        tim.setheading(i * angle)
        tim.color(random_color())
        tim.circle(100)


tim = t.Turtle()
tim.speed(0)
draw_circle(60)

screen = t.Screen()
screen.exitonclick()
