#caesar cipher
from default_alphabet import STR_UP_LIST
from os import system

def caesar(mode,text):
        shift = int(input("How many characters you want to shift? "))
        shift = shift%26
        alph = STR_UP_LIST * 2
        cipher = ""
        if mode == 2:
            shift *= -1
        for i in text:
            if i in alph:
                num = alph.index(i)
                cipher += alph[num+shift]
            else:
                cipher += i
        print(f"\nThe encoded text is: {cipher}")
        again = input("\nDo you want to translate another message?(yes/no) ").upper()

        if again == "YES":
            print(chr(27)+"[2J")
            return True
        else:
            print("\nThanks to use Caesar Cipher translator. Bye!")
            return False

#start
print("--- Welcome to Caesar Cipher translator ---\n")
verif = True
while verif:
    mode = int(input("Select the translation mode below: \n1 - Encryption \n2 - Decryption\nType 1 or 2: "))
    if mode == 1:
        message = input("Write the message you want to encrypt: ").upper()
        verif = caesar(mode,message)
    elif mode == 2:
        message = input("Write the message you want to decrypt: ").upper()
        verif = caesar(mode,message)
    else:
        print("\nThat mode option doesn't exist! Try again.\n")