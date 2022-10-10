from turtle import Turtle, Screen
import random


#colors = ["AliceBlue", "blue", "cyan", "coral", "DeepSkyBlue2", "khaki", "black", "red"]
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# Draw polygon
def draw_polygon(num_of_angle):
    timmy = Turtle()
    color = random.choice(colors)
    timmy.color(color)
    angle = 360 / num_of_angle
    for _ in range(num_of_angle):
        timmy.forward(100)
        timmy.left(angle)

for i in range(3, 10):
    draw_polygon(i)


screen = Screen()
screen.exitonclick()

