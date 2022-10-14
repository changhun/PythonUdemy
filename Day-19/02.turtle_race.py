import turtle as t
import random


# tim = t.Turtle()
screen = t.Screen()
screen.setup(width=500, height=400)

user_bat = screen.textinput(title = "Turtle Game", prompt = "Which turtle win the race? Type color: ")
print(user_bat)

colors = ["Red", "orange", "yellow", "green", "blue", "indigo", "violet"]

turtles = []


def create_rainbow_turtles():
    new_turtles = []

    for color in colors:
        new_turtle = t.Turtle()
        new_turtle.shape("turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtles.append(new_turtle)
    return new_turtles


def move_turtles_to_starting(_turtles):
    for i in range(len(_turtles)):
        _turtles[i].goto(-200, -100 + i * 30)


def is_arrived(turtle):
    return not (turtle.xcor() < 160)


def is_race_end(_turtles):
    for turtle in _turtles:
        if is_arrived(turtle):
            return True
    return False


def random_move(turtle):
    turtle.forward(random.choice(range(1, 10)))


def start_race(_turtles):
    while not is_race_end(_turtles):
        for turtle in _turtles:
            random_move(turtle)


def print_winner(_turtles):
    winner = 0
    for i in range(len(_turtles)):
        if _turtles[i].xcor() > _turtles[winner].xcor():
            winner = i
    print(f"winner is {colors[winner]}")


turtles = create_rainbow_turtles()
move_turtles_to_starting(turtles)
start_race(turtles)
print_winner(turtles)


# 인자 있는 함수를 인자로 받아서 콜해보기.
#def turtle_forward(turtle):
#    turtle.forward(random.choice(range(10, 20)))
#    print(f"xcor: {turtle.xcor()}")


# def turtle_forward():
#     turtles[0].forward(random.choice(range(10, 20)))
#     print(f"xcor: {turtles[0].xcor()}")
#
#
# screen.listen()
# screen.onkey(turtle_forward, "w")

screen.exitonclick()

