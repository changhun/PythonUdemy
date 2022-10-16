import turtle as t
import snake_class
import time
import food
import score_board


screen = t.Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.title("Snake Game@")


snake = snake_class.Snake()
screen.tracer(0)


def is_game_end(_snake):
    # abs(_snake.xcor() > screen.window_width()/2) 이렇게 해도 될 듯
    if _snake.segments[0].xcor() < -screen.window_width()/2 + 20 or _snake.segments[0].xcor() > screen.window_width()/2 - 20:
        print(f"end case1. xcor: {_snake.segments[0].xcor()}")
        return True
    if _snake.segments[0].ycor() < -screen.window_height()/2 + 20 or _snake.segments[0].ycor() > screen.window_height()/2 - 20:
        print("end case 2")
        return True
    return False


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

score = score_board.ScoreBoard()
food = food.Food()
end_of_game = False
while not end_of_game:
    snake.move()
    screen.update()
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.feed()
        score.increasing()

    # Detect collision with wall.
    if is_game_end(snake):
        end_of_game = True

    # Detect collision with tail.
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         end_of_game = True

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            end_of_game = True

    time.sleep(0.1)

score.game_over()
snake.print_segments()

screen.exitonclick()

