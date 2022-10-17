import turtle as t
import random


colors = ['red', 'blue', 'yellow', 'black', 'violet', 'green']


class CarManager:

    def __init__(self):
        self.cars = []
        self.xcor = 300
        self.level = 1
        self.move_distance = 5

    def create_car(self):
        random_value = random.randint(1, 6)
        if random_value == 6:
            new_car = t.Turtle()
            new_car.shape("square")
            new_car.color(random.choice(colors))
            new_car.shapesize(1, 2)
            new_car.setheading(180)
            ycor = random.randint(-250, 250)
            new_car.penup()
            new_car.goto(self.xcor, ycor)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_distance * self.level)

    def collision(self, turtle):
        for car in self.cars:
            #print(f"distance: {car.distance(turtle)}")
            if car.distance(turtle) < 30:
                print("collision")
                return True
        return False

    def level_up(self):
        self.level += 1

    def create_test_car(self, ycor):
        new_car = t.Turtle()
        new_car.shape("square")
        new_car.color(random.choice(colors))
        new_car.shapesize(1, 2)
        new_car.setheading(180)
        new_car.penup()
        new_car.goto(0, ycor)
        return new_car
