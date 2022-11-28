from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Chalkboard", 30, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(position)
        self.keepScore()

    def keepScore(self):
        self.write(
            arg="{}".format(self.score),
            align=ALIGNMENT,
            font=FONT,
        )

    def increaseScore(self):
        self.clear()
        self.score += 1
        self.keepScore()

    def gameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)
        return self.score
