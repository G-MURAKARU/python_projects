import os
from art import logo, celebrate
#HINT: You can call clear() to clear the output in the console.

bids = {}

def winner(theBids):
    bidsList = []
    for key in theBids:
        bidsList.append(theBids[key])
    winningBid = max(bidsList)
    for value in theBids:
        if theBids[value] == winningBid:
            print(celebrate)
            print(f"{value} is the winner with a ${winningBid} bid.")

def auction():
    print(logo)
    bidder = input("What is your name? ")
    amount = int(input("What is your bid? $"))

    bids[bidder] = amount

    next = input("Are there any other bidders? 'yes' or 'no'. ")

    if next == "yes":
        os.system("cls||clear")
        auction()
    else:
        os.system("cls||clear")
        winner(theBids=bids)

auction()
