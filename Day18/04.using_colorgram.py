import colorgram
import turtle as t

tim = t.Turtle()
t.colormode(255)


colors = colorgram.extract("image.jpg", 30)
print(colors)
i = 0
tim.speed(0)

for color in colors:
    print(color.rgb)
    tim.color(color.rgb)
    tim.width(5)
    tim.circle(100)
    tim.setheading(i*30)
    i += 1

screen = t.Screen()
screen.exitonclick()

