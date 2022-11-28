from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Chalkboard", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        with open("highscores.txt", mode="r") as scores:
            for line in scores:
                if line.startswith("highscore:"):
                    lineList = line.split(":")
                    self.highScore = int(lineList[1])
                else:
                    self.highScore = 0

        self.hideturtle()
        self.color("blue")
        self.penup()
        self.goto(0, 260)
        self.keepScore()

    def keepScore(self):
        self.clear()
        self.write(
            arg="Score: {} High Score: {}".format(self.score, self.highScore),
            align=ALIGNMENT,
            font=FONT,
        )

    def increaseScore(self):
        self.score += 1
        self.keepScore()

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("highscores.txt", mode="w") as scores:
                scores.write("highscore:" + str(self.highScore) + "\n")

        self.score = 0
        self.keepScore()

    # def gameOver(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER.", align=ALIGNMENT, font=FONT)
    #     return self.score
