from turtle import Turtle, Screen
import pandas

screen = Screen()
ALIGNMENT = "center"
FONT = ("Roboto Condensed", 12, "normal")


def readStatesCSV():
    states = pandas.read_csv("50_states.csv")

    return states


def stateFinder(statesData):
    statesList = statesData.state.to_list()
    correct = 0
    game = True

    while game:
        if correct == 50:
            game = False
        else:
            stateName = screen.textinput(
                title="{}/50 states correct".format(str(correct)),
                prompt="What's a state's name?",
            ).title()

            if stateName in statesList:
                stateInfo = statesData[statesData.state == stateName]
                xCor = int(stateInfo.x)
                yCor = int(stateInfo.y)

                stateCoordinates = (xCor, yCor)
                screen.tracer(0)
                gameInterface(stateName, stateCoordinates)
                screen.update()

                correct += 1


def gameInterface(stateName, stateCoordinates):
    stateLabel = Turtle()

    stateLabel.hideturtle()
    stateLabel.penup()
    stateLabel.color("black")
    stateLabel.goto(stateCoordinates)
    stateLabel.write(arg=stateName, align=ALIGNMENT, font=FONT)


def main():
    screen.title("United States' States Game")
    screen.bgpic("./blank_states_img.gif")

    statesData = readStatesCSV()

    stateFinder(statesData)

    screen.exitonclick()


if __name__ == "__main__":
    main()
