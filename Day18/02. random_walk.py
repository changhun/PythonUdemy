import turtle as t
import random

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# Draw random work

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.choice(range(0, 255))
    g = random.choice(range(0, 255))
    b = random.choice(range(0, 255))
    rgb = (r, g, b)
    return rgb


def random_walk(move_count):
    for _ in range(move_count):
        #speed = random.choice(range(11))
        speed = 10
        tim.speed(speed)
        # make random color. Two ways
        # color = random.choice(colors)
        # tim.color(color)
        tim.color(random_color())

        direction = random.choice(range(4))
        #tim.right(direction*90)
        tim.setheading(direction*90)
        tim.forward(30)


tim.pensize(10)
random_walk(30)
