#The most famous lottery game in Brazil
import random

def colect_input():
    choices = ['first','second','third','fourth','fifth','sixth']
    for i in range(6):
        pic = int(input(f"Select your {choices[i]} number to bet: "))
        choices[i] = pic
    print("\n")
    choices.sort()
    return choices

def ball_sorter(choices):
    balls = list(range(1,61,1))
    sorted_balls = []
    for i in range(6):
        ball = random.choice(balls)
        sorted_balls.append(ball)
        print(f"Round {i}, the sorted number is... {ball} !")
        balls.remove(ball)
    sorted_balls.sort()
    print(f"\nTherefore, the result is {sorted_balls}\nLet's check your numbers {choices}\n")

    if choices == sorted_balls:
        print("You are very very lucky, you got all the numbers right and win the amazing prize!")
    else:
        checking = []
        for j in range(6):
            check = choices[j] in sorted_balls
            checking.append(check)
        checking = checking.count(True)

        if checking == 5:
            print(f"You are very lucky, you got {checking} numbers right and win the nice prize!")
        elif checking == 4:
            print(f"You are lucky, you got {checking} numbers right and win a prize!")
        elif checking == 3:
            print(f"You were a bit lucky, you got {checking} numbers right! Better luck next time..")
        elif checking == 2:
            print(f"You were not lucky, you got {checking} numbers right! Better luck next time..")
        elif checking == 1:
            print(f"You were a bit unlucky, you got {checking} numbers right! Better luck next time..")
        else:
            print(f"You were very unlucky, you didn't get a single number! Better luck next time..")
        del ball, balls, check, checking

print("Welcome to Mega Sena, a very popular Brazilian lottery game.\n")
print("The rules are simple, try to guess 6 numbers of prize drawing. The numbers range from 1 to 60.\n\n")
choices = colect_input()
ball_sorter(choices)
