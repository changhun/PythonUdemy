from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.refresh()

    def refresh(self):
        # xcor = random.randint(-280, 280) + 5
        # ycor = random.randint(-280, 280) + 5
        xcor = random.randint(-280, 280)
        ycor = random.randint(-280, 280)
        xcor -= xcor % 20
        ycor -= ycor % 20
        self.goto(xcor, ycor)

