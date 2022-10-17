import turtle as t
from player import Player
import time
from car_manager import CarManager
from score_board import ScoreBoard


screen = t.Screen()
screen.title("Turtle Crossing Game@@")
screen.setup(600, 600)
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreBoard = ScoreBoard()

screen.listen()
screen.onkey(player.move, "Up")
screen.onkeypress(player.move, "Up")


# car = carManager.create_test_car(-250)
# car.goto(0, -250)
# car.goto(30, -280)
# print(car.distance(player))
# screen.update()

end_of_game = False
while not end_of_game:
    if player.end_of_line():
        player.go_starting_point()
        carManager.level_up()
        scoreBoard.level_up()

    if carManager.collision(player):
        scoreBoard.game_over()
        end_of_game = True

    carManager.create_car()
    carManager.move_cars()
    screen.update()
    time.sleep(0.1)


screen.exitonclick()