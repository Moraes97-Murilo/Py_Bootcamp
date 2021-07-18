#Now this bootcamp is getting interesting
#18/07/2021
import random

def card_dealer():
    '''Returns a random card from the deck.'''
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    c = random.choice(cards)
    return c

player_set, pc_set = [], []

for _ in range(2):
    player_set.append(card_dealer())
    pc_set.append(card_dealer())

