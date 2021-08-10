#wich number is higher?
#new project
import random, data, time, traceback

def get_data(data_f,diff):
    '''Difficulty of the game.'''
    #print(data_f)
    data_values = list(data.full_data.keys())
    names = data_f[data_values[diff]]["name"]
    descs = data_f[data_values[diff]]["description"]
    amounts = data_f[data_values[diff]]["amount"]
    choicee = random.randint(0,len(names)-1)

    choice = [descs,names[choicee],amounts[choicee]]
    data_f[data_values[diff]]["name"].remove(names[choicee])
    data_f[data_values[diff]]["amount"].remove(amounts[choicee])
    #print(data_f)
    #print(choice)

    return data_f, choice

def try_resp(score,res,v1,v2):
    time.sleep(1)
    if res == 1:
        if v1 > v2:
            print("You're right!")
            score +=1
            time.sleep(2)
        else:
            print("You're wrong!")
            time.sleep(2)
    elif res == 2:
        if v1 < v2:
            print("You're right!")
            score +=1
            time.sleep(2)
        else:
            print("You're wrong!")
            time.sleep(2)
    else:
        print("You type something wrong..Please learn how to play, goodbye!")
        time.sleep(5)
    print(chr(27) + "[2J")
    return score


print("\nWelcome to my awesome guessing game!\n\n")
score = 0
inicial = "Let's start! "
STATEMENT = "Your current score is "
ACTUAL = "Answer 1 or 2... Wich one is higher? \n"
game = True
data_f = data.full_data

while game:
    print(inicial+STATEMENT+f"{score}.\n")
    try:
        if score == 0:
            diffi = 0
            data_f, values1 = get_data(data_f, diffi)
            values1.append(1)
            data_f, values2 = get_data(data_f, diffi)
            values2.append(2)
            resp = int(input(ACTUAL+"1) "+values1[0]+values1[1]+"\n or \n2)"+values2[0]+values2[1]+": "))
            time.sleep(1)
            score_re = try_resp(score,resp,values1[2],values2[2])
            if score_re > score:
                inicial = "Congratulations! "
                score = score_re
            else:
                print("You lost the game, better luck next time.")
                game = False

        elif score < 3:
            diffi = 0
            if resp == values1[3]:
                pass
            else:
                values1 = values2
                values1[3] = 1
            data_f, values2 = get_data(data_f, diffi)
            values2.append(2)
            resp = int(input(ACTUAL+"1) "+values1[0]+values1[1]+"\n or \n2)"+values2[0]+values2[1]+": "))
            time.sleep(1)
            score_re = try_resp(score,resp,values1[2],values2[2])
            if score_re > score:
                inicial = "Congratulations! "
                score = score_re
            else:
                print("You lost the game, better luck next time.")
                game = False

        elif score < 7:
            diffi = 1
            if resp == values1[3]:
                pass
            else:
                values1 = values2
                values1[3] = 1
            data_f, values2 = get_data(data_f, diffi)
            values2.append(2)
            resp = int(input(ACTUAL+"1) "+values1[0]+values1[1]+"\n or \n2)"+values2[0]+values2[1]+": "))
            time.sleep(1)
            score_re = try_resp(score,resp,values1[2],values2[2])
            if score_re > score:
                inicial = "Congratulations! "
                score = score_re
            else:
                print("You lost the game, better luck next time.")
                game = False
        else:
            diffi = 2
            if resp == values1[3]:
                pass
            else:
                values1 = values2
                values1[3] = 1
            data_f, values2 = get_data(data_f, diffi)
            values2.append(2)
            resp = int(input(ACTUAL+"1) "+values1[0]+values1[1]+"\n or \n2)"+values2[0]+values2[1]+": "))
            time.sleep(1.5)
            score_re = try_resp(score,resp,values1[2],values2[2])
            if score_re > score:
                inicial = "Congratulations! "
                score = score_re
            else:
                print("You lost the game, better luck next time.")
                game = False
    except:
        print(chr(27) + "[2J")
        print("You finish the game, YOU'RE AWESOME!!!")
        time.sleep(5)
        game = False