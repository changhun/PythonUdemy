import colorgram
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


colors = colorgram.extract("image.jpg", 30)

# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r, g, b)
#     rgb_colors.append(rgb_color)
#
# print(rgb_colors)

rgb_colors = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]

tim.hideturtle()
for y in range(10):
    for x in range(10):
        tim.penup()
        tim.setpos(x*50 - 225, y*50 - 225)
        tim.pendown()
        tim.dot(20, random.choice(rgb_colors))


screen = t.Screen()
screen.exitonclick()
