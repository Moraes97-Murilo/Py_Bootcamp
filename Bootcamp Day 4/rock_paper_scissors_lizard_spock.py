#The game played in THE BIG BANG THEORY tv show
import random, time

def show_choices(options):
    print_option = []
    for i in options:
        if i == "ROCK":
            print_option.append("rock💎rock")
        elif i == "PAPER":
            print_option.append("paper📄paper")
        elif i == "SCISSORS":
            print_option.append("scissors✂️scissors")
        elif i == "LIZARD":
            print_option.append("lizard🦎lizard")
        else:
            print_option.append("spock🖖spock")  
    print(print_option[0])
    print("x")
    print(print_option[1])
    del print_option
def decide_win(options):
    if options[0] == "ROCK":
        if options[1] == "ROCK":
            return 0, "DRAW"
        elif options[1] == "PAPER":
            return 1, "YOU LOOSE!"
        elif options[1] == "SCISSORS":
            return 2, "YOU WIN!"
        elif options[1] == "LIZARD":
            return 3, "YOU WIN!"
        else:
            return 4, "YOU LOOSE!"
    elif options[0] == "PAPER":
        if options[1] == "ROCK":
            return 1, "YOU WIN!"
        elif options[1] == "PAPER":
            return 0, "DRAW"
        elif options[1] == "SCISSORS":
            return 5, "YOU LOOSE!"
        elif options[1] == "LIZARD":
            return 6, "YOU LOOSE!"
        else:
            return 7, "YOU WIN!"
    elif options[0] == "SCISSORS":
        if options[1] == "ROCK":
            return 2, "YOU LOOSE!"
        elif options[1] == "PAPER":
            return 5, "YOU WIN!"
        elif options[1] == "SCISSORS":
            return 0, "DRAW"
        elif options[1] == "LIZARD":
            return 8, "YOU WIN!"
        else:
            return 9, "YOU LOOSE!"
    elif options[0] == "LIZARD":
        if options[1] == "ROCK":
            return 3, "YOU LOOSE!"
        elif options[1] == "PAPER":
            return 6, "YOU WIN!"
        elif options[1] == "SCISSORS":
            return 8, "YOU LOOSE!"
        elif options[1] == "LIZARD":
            return 0, "DRAW"
        else:
            return 10, "YOU WIN!"
    else:
        if options[1] == "ROCK":
            return 4, "YOU WIN!"
        elif options[1] == "PAPER":
            return 7, "YOU LOOSE!"
        elif options[1] == "SCISSORS":
            return 9, "YOU WIN!"
        elif options[1] == "LIZARD":
            return 10, "YOU LOOSE!"
        else:
            return 0, "DRAW"
def cool_phrase(results,options):
    if options == 1:
        print(f"\nPAPER covers ROCK...{results}\n")
    elif options == 2:
        print(f"\nROCK crushes SCISSORS...{results}\n")
    elif options == 3:
        print(f"\nROCK crushes LIZARD...{results}\n")
    elif options == 4:
        print(f"\nSPOCK vaporizes ROCK...{results}\n")
    elif options == 5:
        print(f"\nSCISSORS cuts PAPER...{results}\n")
    elif options == 6:
        print(f"\nLIZARD eats PAPER...{results}\n")
    elif options == 7:
        print(f"\nPAPER disproves SPOCK...{results}\n")
    elif options == 8:
        print(f"\nSCISSORS decapitates LIZARD...{results}\n")
    elif options == 9:
        print(f"\nSPOCK smashes SCISSORS...{results}\n")
    else:
        print(f"\nLIZARD poisons SPOCK...{results}\n")

#Start
print("\n--- ROCK_PAPER_SCISSORS_LIZARD_SPOCK ---\n\n\
Welcome to the best decision game!")

p_verif = True

while p_verif:
    options = ["ROCK","PAPER","SCISSORS","LIZARD","SPOCK"]
    comp_choice = random.choice(options)
    player_choice = (input("Now choose between: ROCK, PAPER, SCISSORS, LIZARD, SPOCK... ")).upper()

    if player_choice in options:
        options = [player_choice, comp_choice]
        print("3...")
        time.sleep(0.25)
        print("    2...")
        time.sleep(0.25)
        print("        1...\n")
        show_choices(options)
        options, results = decide_win(options)
        if options != 0:
            cool_phrase(results,options)
            p_verif = False
        else:
            print("\nIt's a draw, try again!\n\n")
    else:
        print("\nPlease, you must choose a valid option!\n\n")