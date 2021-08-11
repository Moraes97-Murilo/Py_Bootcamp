#I've accidentally skip to the higher lower game grrrrrr
from random import randint
import time

def check_guess(randnum,gnum):
    if gnum ==  randnum:
        print("\nFinally! You're a crazy one, like me... and...")
        time.sleep(1.5)
        print('You win!!!\n\n\n')
        return True
    elif gnum > randnum:
        print("\nStop being a silly, you must be CRAZY to win this game... and...")
        time.sleep(1.8)
        print('The number is lower than your guess! You silly!')
        return False
    else:
        print("\nStop being a fool, you must be CRAZY to win this game... and...")
        time.sleep(1.8)
        print('The number is higher than your guess! You fool!')
        return False
print('\nWelcome to my Crazy Guessing Game!\n\n')
game = True
while game:
    diff = input('Select the difficulty: \na)easy\nb)medium\nc)hard\nd)crazy\n--> ').lower()
    num = randint(1,100)
    turns = 0
    if diff == 'a' or diff == 'easy':
        turns = 10
    elif diff == 'b' or diff == 'medium':
        turns = 7
    elif diff == 'c' or diff == 'hard':
        turns = 5
    elif diff == 'd' or diff == 'crazy':
        turns = 3
    else:
        print('You type something wrong, game is restarting...')
    
    try:
        for i in range(0,turns):
            guess = int(input(f'{i+1}°try - Guess a number between 1 and 100: '))
            check = check_guess(num,guess)
            if i == (turns-1):
                time.sleep(1)
                print(chr(27) + "[2J")
                print("Your attempts are over, you're NOT CRAZY just IDIOT!!")
                time.sleep(7)
            elif check == False:
                pass
            else:
                again = input('\nDo you wanna play again? \na)yes\nb)no\n---> ')
                if again == "b" or again == "no" or again == "n":
                    game = False
                break
        print(chr(27) + "[2J")
    except:
        print(chr(27) + "[2J")