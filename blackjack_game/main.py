import os
import random

from art import logo


def playerChoice():
    playMove = input(
        "\nWhat are you going to do? Hit or stand? \nType 'y' to hit (pick another card) or 'n' to stand (pass to computer). "
    )

    if playMove != "y":
        return False
    else:
        return True


def dealCard(player, myturn):
    move = playerChoice()

    if move:
        player.append(random.choice(cards))

        print(f"\n Your new hand is {player} = {sum(player)}.")

        if sum(player) > 21 and player.count(11):
            player[player.index(11)] = 1
            print(
                f"Value of ace is now 1 instead of 11. \nYour new hand is {player} = {sum(player)}."
            )
            dealCard(player, myturn)

        elif sum(player) >= 21:
            pass

        else:
            dealCard(player, myturn)
    else:
        pass

    return player


def compTurn(p1, comp):
    turn = True

    if sum(comp) == 21:
        print(f" The dealer's final hand: {comp}, total: 0.")
        return "Computer wins"

    while turn:
        if sum(comp) < 17:
            comp.append(random.choice(cards))
        elif sum(comp) > 21 and comp.count(11):
            comp[comp.index(11)] = 1
        elif sum(comp) > 21:
            print(f" The dealer's final hand: {comp}, total: {sum(comp)}.")
            return "Player wins"

        elif sum(comp) > sum(p1):
            print(f" The dealer's final hand: {comp}, total: {sum(comp)}.")
            return "Computer wins"

        elif sum(comp) < sum(p1):
            comp.append(random.choice(cards))

        elif sum(comp) == sum(p1):
            print(f" The dealer's final hand: {comp}, total: {sum(comp)}.")
            return "Draw"

        else:
            comp.append(random.choice(cards))


def blackjack():
    playerHand = []
    compHand = []

    print(logo)

    while len(playerHand) < 2:
        playerHand.append(random.choice(cards))
        compHand.append(random.choice(cards))

    print(f" Your current hand is {playerHand}, total = {sum(playerHand)}")
    print(f" The dealer's first card = {compHand[0]}")

    if sum(playerHand) == 21:
        print(f"Your hand {playerHand} = 0 is a Blackjack!! \n You win!")

    elif sum(compHand) == 21:
        print(f"The dealer's hand {compHand} = 0 is a Blackjack!! \n Computer wins... ")

    else:
        playerTurn = True
        finalPlayerHand = dealCard(playerHand, playerTurn)

        if sum(finalPlayerHand) >= 21:
            print(
                f"\n Your final hand: {finalPlayerHand}, total: {sum(finalPlayerHand)}."
            )
            print(f" The dealer's final hand: {compHand}, total: {sum(compHand)}.")

            if sum(finalPlayerHand) == 21:
                print("You win!! 😎y")
            else:
                print("You went overboard. You lose. 🤧")

        else:
            print(
                f" Your final hand: {finalPlayerHand}, total: {sum(finalPlayerHand)}."
            )
            score = compTurn(finalPlayerHand, compHand)

            if score == "Player wins":
                print("You win!! 😎")
            elif score == "Computer wins":
                print("Computer wins... 😪")
            elif score == "Draw":
                print("It's a draw. 🤷🏽‍♀️")

    play = input(
        "\nDo you want to play another game of blackjack? \nType 'y' for yes, 'n' for no. "
    )
    if play == "y":
        os.system("cls||clear")
        blackjack()


cards = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
play = input(
    "Do you want to play a game of blackjack? \nType 'y' for yes, 'n' for no. "
)

if play == "y":
    os.system("cls||clear")
    blackjack()
