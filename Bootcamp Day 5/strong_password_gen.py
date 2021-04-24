#In this code the position of type of character must be random too
import random
STRING_LIST = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
NUMBER_LIST = [0,1,2,3,4,5,6,7,8,9]
SYMBOL_LIST = ['-','+','@','#','=','(',')','/','%','&']

print("--- Welcome to the best password generator! ---\n")
min_char = int(input("Type the minimum number of character the password must be: "))
max_char = int(input("Now, type the maximum number of character the password must be: "))

if min_char == max_char:
    pass
elif min_char > max_char:
    temp = min_char
    min_char = max_char
    max_char = temp
    del temp
    min_char = random.choice(range(min_char,max_char,1))
else:
    min_char = random.choice(range(min_char,max_char,1))

del max_char

#filters of variables type

