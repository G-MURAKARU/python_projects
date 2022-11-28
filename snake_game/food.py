from turtle import Turtle, Screen
import random


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.reset()
        self.shape("turtle")
        self.color("red")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.spawn()

    def spawn(self):
        self.screen = Screen()
        xCoor = random.randint(-105, 105)
        yCoor = random.randint(-260, 260)
        self.goto(xCoor, yCoor)
        self.screen.update()
