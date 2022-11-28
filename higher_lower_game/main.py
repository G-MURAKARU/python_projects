import os
import random

from art import logo, vs
from gameData import data

# randomly pick two elements from data, which is a list of dictionaries, and save them (perhaps in a two-element list..?)
def choicesList(data, choices):
    """Forms a list of two elements that will be displayed to the user for comparison"""

    while len(choices) < 2:
        choices.append(random.choice(data))

    if choices[0] == choices[1]:
        choices.pop()
        choicesList(data, choices)

    return choices


# once the random elements have been chosen, display key[values] as a sentence
def sentenceGen(choices):
    """Generates a printable, readable form of the data got from gameData"""
    people = []
    for person in choices:
        vowels = ["A", "E", "I", "O", "U"]
        if person["description"][0] in vowels:
            article = "an"
        else:
            article = "a"

        people.append(
            "{}, {} {}, from {}.".format(
                person["name"], article, person["description"], person["country"]
            )
        )

    print("Compare A: {}\n{}\nAgainst B: {}".format(people[0], vs, people[1]))


# ask user who they think has more Instagram followers, compare the two
def comparison(choices, playerTurn):
    """Gets the number of personalities' followers, compares them with the user's guess"""
    followers = []
    for person in choices:
        followers.append(person["follower_count"])

    answer = max(followers)

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    if guess == "A":
        guessIndex = 0
    elif guess == "B":
        guessIndex = 1

    if guessIndex != followers.index(answer):
        playerTurn = False

    return playerTurn


print(logo)

# if True, game goes on. if False, game is over - create a variable that stores this, and a variable to store the player's score
playerTurn = True
playerScore = 0

choices = []

while playerTurn:
    choices = choicesList(data, choices)
    sentenceGen(choices)
    playerTurn = comparison(choices, playerTurn)

    # clear the screen/terminal after each correct turn
    os.system("cls||clear")

    print(logo)

    if playerTurn:
        # increase the player score after each correct answer
        playerScore += 1

        print("You're right! Current score: {}.".format(playerScore))

        # if we use a list, we should pop list[0] after each round (easier to keep track of than reassignment)
        choices.pop(0)

print("Well. That's wrong. Game over. Final score: {}".format(playerScore))
