#The game played in THE BIG BANG THEORY tv show

import random, time

options = ["ROCK","PAPER","SCISSORS","LIZARD","SPOCK"]

print("\n--- ROCK_PAPER_SCISSORS_LIZARD_SPOCK ---\n\n\
Welcome to the best decision game!\n\
Choose between: ROCK, PAPER, SCISSORS, LIZARD, SPOCK")

player = (input("And try to win the computer choice...\n")).upper()
p_verif = True

while p_verif:
    if player in options:
        p_verif = False
    else:
        print("Please, you must choose a valid option!")
        player = (input("Now choose between: ROCK, PAPER, SCISSORS, LIZARD, SPOCK... ")).upper()

print("The result is down below...")