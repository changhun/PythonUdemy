import turtle as t
import random


ALIGN = 'left'
FONT = ('Arial', 20, 'normal')

# tim = t.Turtle()
WIDTH = 1000
HEIGHT = 400

screen = t.Screen()
#screen.setup(width=500, height=400)
screen.setup(width=WIDTH, height=HEIGHT)

user_bat = screen.textinput(title="Turtle Game", prompt="Which turtle win the race? Type color: ")
print(user_bat)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

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
    for i in range(len(_turtles) - 1,  -1, -1):
        _turtles[i].goto(-screen.window_width()/2 + 100, -100 + i * 30)


def is_arrived(turtle, end_line):
    return not (turtle.xcor() < end_line)


def is_race_end(_turtles):
    end_line = screen.window_width()/2 - 100
    for turtle in _turtles:
        if is_arrived(turtle, end_line):
            return True
    return False


def race_almost_end(_turtles, end_line):
    for turtle in _turtles:
        if turtle.xcor() >= end_line - 100:
            return True
    return False


def random_move(turtle):
    turtle.forward(random.randint(0, 10))


def random_slow_move(turtle):
    random_distance = random.random() * 2
    turtle.forward(random_distance)
    #print(f"distance: {random_distance}")


def start_race(_turtles):
    end_line = screen.window_width()/2 - 100
    while not race_almost_end(_turtles, end_line):
        for turtle in _turtles:
            random_move(turtle)

    while not is_race_end(_turtles):
        for turtle in _turtles:
            random_slow_move(turtle)


def print_winner(_turtles):
    winner = 0
    for i in range(len(_turtles)):
        if _turtles[i].xcor() > _turtles[winner].xcor():
            winner = i
    print(f"winner is {colors[winner]}")
    print(f"turtle's color: {_turtles[winner].color()[0]}")
    turtle = t.Turtle()
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-130, 0)

    # turtle.color() returns tuple like ('red', 'red')
    if user_bat == _turtles[winner].color()[0]:
        turtle.write(f"Winner is {_turtles[winner].color()[0]}. You win!!", align=ALIGN, font=FONT)
    else:
        turtle.write(f"Winner is {_turtles[winner].color()[0]}. You lose.", align=ALIGN, font=FONT)


def line_drawing():
    turtle = t.Turtle()
    turtle.shape("turtle")
    turtle.width(5)
    turtle.penup()
    turtle.goto(screen.window_width()/2 - 100, screen.window_height()/2 - 50)
    turtle.pendown()
    turtle.setheading(-90)
    turtle.forward(screen.window_height() - 100)


def speed_up():
    selected_turtle.forward(5)
    print(f"{selected_turtle.color()} turtle boost up")


screen.listen()

line_drawing()
turtles = create_rainbow_turtles()
move_turtles_to_starting(turtles)

selected_turtle = turtles[colors.index(user_bat)]
screen.onkey(speed_up, "a")
start_race(turtles)
print_winner(turtles)

# ?????? ?????? ????????? ????????? ????????? ????????????.
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

