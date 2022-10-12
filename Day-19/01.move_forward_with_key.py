import turtle as t


tim = t.Turtle()
screen = t.Screen()


def move_forward():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()


# Higher order Function concept. In this example, calc() function is higher order function.
# def add(a, b):
#     return a + b
#
#
# def sub(a, b):
#     return a - b
#
#
# def multi(a, b):
#     return a * b
#
#
# def div(a, b):
#     return a/b
#
#
# def calc(a, b, func):
#     return func(a, b)
#
#
# ret = calc(10, 13, add)
# print(ret)