import turtle as t
import snake_class
import time

screen = t.Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.title("Snake Game@")


snake = snake_class.Snake()
screen.tracer(0)


def is_game_end(_snake):
    # abs(_snake.xcor() > screen.window_width()/2) 이렇게 해도 될 듯
    if _snake.segments[0].xcor() < -screen.window_width()/2 or _snake.segments[0].xcor() > screen.window_width()/2:
        print(f"end case1. xcor: {_snake.segments[0].xcor()}")
        return True
    if _snake.segments[0].ycor() < -screen.window_height()/2 or _snake.segments[0].ycor() > screen.window_height()/2:
        print("end case 2")
        return True
    return False


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

end_of_game = False
while not end_of_game:
    snake.move()
    screen.update()
    if is_game_end(snake):
        end_of_game = True
    time.sleep(0.1)

screen.exitonclick()

