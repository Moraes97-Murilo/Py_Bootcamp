#Now this bootcamp is getting interesting
#18/07/2021
import random

def card_dealer():
    '''Returns a random card from the deck.'''
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    c = random.choice(cards)
    return c
def score_filt(card_set):
    '''Look for an instantaneous BlackJack or returns the score.'''
    if sum(card_set) == 21:
        return 0
    elif 11 in card_set and sum(card_set) > 21:
        card_set.remove(11)
        card_set.append(1)
        return sum(card_set)
    else:
        return sum(card_set)

player_set, pc_set, game_status = [], [], True
    
for _ in range(2):
    player_set.append(card_dealer())
    pc_set.append(card_dealer())

while game_status:

    player_score, pc_score = score_filt(player_set), score_filt(pc_set)

    print(f"In your hands have this cards: {player_set}!")
    print(f"Dealer's first card is {pc_set[0]}")

    if player_score > 21 or pc_score == 0:
        print(f"Your score is {player_score} and the Dealer score is {pc_score}.")
        print("You lost!")
        game_status = False

    elif player_score == 0:
        print("You got a blackJack! It's your win!")
        game_status = False

    else:
        luck = input("Type P to pass or anyone to get another card: ").upper()
        if luck == "P":
            print(f"Your score is {player_score} and the Dealer score is {pc_score}.")
            if player_score > pc_score:
                print("You win!")
                game_status = False
            elif pc_score > player_score:
                print("You lost!")
                game_status = False
            else:
                print("It's a draw!")
                game_status = False
        else:
            player_set.append(card_dealer())
            pc_set.append(card_dealer())
