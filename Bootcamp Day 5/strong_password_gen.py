#In this code the position of type of character must be random too
import random
import default_alphabet

def random_charactering(limit,answer):
    type_list = []
    if answer == 'YES':
        a = random.choice(range(limit//2,limit,1))
        if a != limit:
            b = limit - a
            type_list.append(a)
            type_list.append(b)
        else:
            a -= 1
            b = 1
            type_list.append(a)
            type_list.append(b)
    else:
        key_value = round(limit*0.8)
        a = random.choice(range(limit//2,limit,1))
        if a != limit:
            key_value = (limit - a)//2
            b = random.choice(range(key_value,limit-a,1))
            if (b+a) != limit:
                c = limit - a - b
                type_list.append(a)
                type_list.append(b)
                type_list.append(c)
            else:
                if a <= b:
                    b -= 1
                    c = 1
                    type_list.append(a)
                    type_list.append(b)
                    type_list.append(c)
                else:
                    a -= 1
                    c = 1
                    type_list.append(a)
                    type_list.append(b)
                    type_list.append(c)
        else:
            a -= 2
            b = 1
            type_list.append(a)
            type_list.append(b)
            type_list.append(c)

    return type_list

#start
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
excep1 = (input("\nNow, answer YES or NO...Your password must have only numbers? ")).upper()
if excep1 == 'YES':
    pass
else:
    excep2 = (input("\nAgain, answer YES or NO...Your password must have only numbers and letters? ")).upper()
    if excep2 == 'YES':
        type_list = random_charactering(min_char, excep2)
    else:
        type_list = random_charactering(min_char, excep2)

#main
password = ''
if excep1 == 'YES':
    for i in range(0,min_char,1):
        a = random.choice(default_alphabet.NUMBER_LIST)
        password += a
else:
    if excep2 == 'YES': #STRNUM_LIST
        if type_list[0] > 1:
            key_num1 = type_list[0] // 2
            key_num2 = type_list[0] - key_num1
            for i in range(0,key_num2,1):
                a = random.choice(default_alphabet.STR_UP_LIST)
                password += a
            for j in range(0,key_num1,1):
                a = random.choice(default_alphabet.STR_LO_LIST)
                password += a
            for k in range(0,type_list[1],1):
                a = random.choice(default_alphabet.NUMBER_LIST)
                password += a
        else:
            for i in range(0,type_list[0],1):
                a = random.choice(default_alphabet.STR_UP_LIST)
                password += a
            for j in range(0,type_list[1],1):
                a = random.choice(default_alphabet.NUMBER_LIST)
                password += a
    else:
        if type_list[0] > 1:
            key_num1 = type_list[0] // 2
            key_num2 = type_list[0] - key_num1
            for i in range(0,key_num2,1):
                a = random.choice(default_alphabet.STR_UP_LIST)
                password += a
            for j in range(0,key_num1,1):
                a = random.choice(default_alphabet.STR_LO_LIST)
                password += a
            for k in range(0,type_list[1],1):
                a = random.choice(default_alphabet.NUMBER_LIST)
                password += a
            for l in range(0,type_list[2],1):
                a = random.choice(default_alphabet.SYMBOL_LIST)
                password += a
        else:
            for i in range(0,type_list[0],1):
                a = random.choice(default_alphabet.STR_UP_LIST)
                password += a
            for j in range(0,type_list[1],1):
                a = random.choice(default_alphabet.NUMBER_LIST)
                password += a
            for k in range(0,type_list[2],1):
                a = random.choice(default_alphabet.SYMBOL_LIST)
                password += a
password = ''.join(random.sample(password,len(password)))
print(f"Your best password is:    {password}")