import random
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position, 0)

    def goUp(self):
        yCor = self.ycor() + 20
        self.goto(self.xcor(), yCor)

    def goDown(self):
        yCor = self.ycor() - 20
        self.goto(self.xcor(), yCor)
