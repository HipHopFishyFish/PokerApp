"""this is the card dealer so i can deal cards ayayyayayayayyayy siuuuuuu"""

import cardsModule as cm


def dealPlayers(cards, num):
    playercards = []
    for i in range(num):
        playercards.append([cards.cards.pop(len(cards.cards)-1), cards.cards.pop(len(cards.cards)-1)])
    return playercards
        
def flop(cards):
    cards.cards.pop(len(cards.cards)-1)

    flopcards = [cards.cards.pop(len(cards.cards)-1), cards.cards.pop(len(cards.cards)-1), cards.cards.pop(len(cards.cards)-1)]
    return flopcards

def single(cards):
    cards.cards.pop(len(cards.cards)-1)

    return cards.cards.pop(len(cards.cards)-1)
