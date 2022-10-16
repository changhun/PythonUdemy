import turtle as t
from paddle import Pad
from ball import Ball
from score_board import ScoreBoard
import time


INITIAL_POSITION = [(-390, 0), (380, 0)]
SCOREBOARD_POSITIONS = [(-250, 270), (150, 270)]

screen = t.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()


def reset_screen(_screen):
    screen.clearscreen()
    screen.bgcolor("black")
    screen.tracer(0)


scoreBoard1 = ScoreBoard(SCOREBOARD_POSITIONS[0])
scoreBoard2 = ScoreBoard(SCOREBOARD_POSITIONS[1])


def start_game():
    pad1 = Pad(INITIAL_POSITION[0])
    pad2 = Pad(INITIAL_POSITION[1])
    screen.onkey(pad1.up, "w")
    screen.onkey(pad1.down, "s")
    screen.onkey(pad2.up, "Up")
    screen.onkey(pad2.down, "Down")

    ball = Ball()
    end_of_game = False
    while not end_of_game:
        ball.move()
        # bounce when upper or lower screen collision
        if ball.ycor() >= 280 or ball.ycor() <= -280:
            ball.bounce()
        # bounce when the collision with paddle
        if ball.distance(pad1) < 50 and ball.xcor() <= -370:
            ball.bounce_collision()
        elif ball.distance(pad2) < 50 and ball.xcor() >= 360:
            ball.bounce_collision()

        # Detect collision with side wall
        if ball.xcor() >= 380:
            scoreBoard1.score_up()
            end_of_game = True
        elif ball.xcor() <= -390:

            scoreBoard2.score_up()
            end_of_game = True

        screen.update()
        time.sleep(0.05)


while True:
    start_game()
    reset_screen(screen)
    scoreBoard1.show()
    scoreBoard2.show()

screen.exitonclick()
