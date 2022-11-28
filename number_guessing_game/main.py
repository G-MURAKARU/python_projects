# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import art

answer = random.randint(1, 100)
print(answer)
easyMode = 10
hardMode = 5


def setDifficulty(diff):
    if diff == "easy":
        print("\nYou have 10 lives.")
        return easyMode
    elif diff == "hard":
        print("\nYou have 5 lives.")
        return hardMode
    else:
        print("\nNext time, pick a valid difficulty.")
        guessingGame(answer)


def checkAnswer(answer, guess, lives):
    """Checks answer against guess; returns number of remaining lives."""
    if guess == answer and lives > 0:
        print(
            "\nYou were lucky, you had {} lives left. The answer is indeed, {}.".format(
                lives, answer
            )
        )
        return 0
    elif guess != answer and lives > 0:
        lives -= 1
        if lives == 0:
            print("\nYou have {} lives left.\nDarkness has arrived.".format(lives))
            return lives
        elif guess > answer:
            print(
                "\nYour guess is too high.\nThe end is near, you have {} lives left. Guess again.".format(
                    lives
                )
            )
        elif guess < answer:
            print(
                "\nYour guess is too low.\nThe end is near, you have {} lives left. Guess again.".format(
                    lives
                )
            )
        return lives


def guessingGame(answer):
    diff = input("Pick a difficulty, easy or hard? ")

    lives = setDifficulty(diff)

    print("\nPick a number between 1 and 100...")

    while lives > 0:
        guess = int(input("\nWhat's your guess? "))

        lives = checkAnswer(answer, guess, lives)


print(art.logo)
print("\nThey called me a mad man... time to play.")
guessingGame(answer)
