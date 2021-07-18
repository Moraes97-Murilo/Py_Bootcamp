#Now this bootcamp is getting interesting
#18/07/2021
import random

def card_dealer():
    '''Returns a random card from the deck.'''
    cards = [11,2,3,4,5,6,7,8,9,10]
    c = random.choice(cards)
    return c

player_set, pc_set = [], []

for i in range(4):
    dealer_outp = card_dealer()
    if i%2 == 0:
        player_set.append(dealer_outp)
    else:
        pc_set.append(dealer_outp)