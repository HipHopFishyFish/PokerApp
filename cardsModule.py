"""this is the cards module for my poker thing

aaa woohoo yay
"""

import random

HEARTS   = "hearts"
SPADES   = "spades"
DIAMONDS = "diamonds"
CLUBS    = "clubs"

suits = [HEARTS, SPADES, DIAMONDS, CLUBS]

ACE   = "ace"
TWO   = "two"
THREE = "three"
FOUR  = "four"
FIVE  = "five"
SIX   = "six"
SEVEN = "seven"
EIGHT = "eight"
NINE  = "nine"
TEN   = "ten"
JACK  = "jack"
QUEEN = "queen"
KING  = "king"

numbers = [ACE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING]

class Card:
    def __init__(self, number, suit):
        self.suit = suit
        self.number = number
        # self.img = img
    
    def __repr__(self):
        return f"{self.number.capitalize()} of {self.suit.capitalize()}"

class Cards:
    def __init__(self, *cards):
        self.cards = list(cards)

    def addCard(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

def makeCards(shuffled = True):
    cards = Cards()
    for suit in suits:
        for num in numbers:
            cards.addCard(Card(num, suit))
    if shuffled:
        cards.shuffle()
    return cards
