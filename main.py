############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


from art import logo
from replit import clear
import random

def playerChoice():
    playMove = input("\nWhat are you going to do? Hit or stand? \nType 'y' to hit (pick another card) or 'n' to stand (pass to computer). ")

    if playMove != 'y':
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
            print(f"Value of ace is now 1 instead of 11. \nYour new hand is {player} = {sum(player)}.")
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
            print(f"\n Your final hand: {finalPlayerHand}, total: {sum(finalPlayerHand)}.")
            print(f" The dealer's final hand: {compHand}, total: {sum(compHand)}.")

            if sum(finalPlayerHand) == 21:
                print("You win!! 😎y")
            else:
                print("You went overboard. You lose. 🤧")

        else:
            print(f" Your final hand: {finalPlayerHand}, total: {sum(finalPlayerHand)}.")
            score = compTurn(finalPlayerHand, compHand)

            if score == "Player wins":
                print("You win!! 😎")
            elif score == "Computer wins":
                print("Computer wins... 😪")
            elif score == "Draw":
                print("It's a draw. 🤷🏽‍♀️")

    play = input("\nDo you want to play another game of blackjack? \nType 'y' for yes, 'n' for no. ")
    if play == 'y':
        clear()
        blackjack()


cards = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
play = input("Do you want to play a game of blackjack? \nType 'y' for yes, 'n' for no. ")

if play == 'y':
    clear()
    blackjack()