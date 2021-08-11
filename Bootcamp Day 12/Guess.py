#I've accidentally skip to the higher lower game grrrrrr
from random import randint

print('\nWelcome to my Crazy Guessing Game!\n\n')
game = True
while game:
    diff = input('Select the difficulty: \na)easy\nb)medium\nc)hard\nd)crazy\n--> ').lower()
    num = randint(1,100)
    turns = 0
    if diff == 'a' or diff == 'easy':
        turns = 10
        print()
    elif diff == 'b' or diff == 'medium':
        turns = 7
        print()
    elif diff == 'c' or diff == 'hard':
        turns = 5
        print()
    elif diff == 'd' or diff == 'crazy':
        turns = 3
        print()
    else:
        print