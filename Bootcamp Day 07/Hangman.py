#This project will use a bunch of loops
from man import man
import random, words

categories = words.categories
category = random.choice(list(categories.keys()))
word = random.choice(categories[category])
sub_list = []
for i in word:
    if i != " ":
        sub_list.append('_')
    else:
        sub_list.append(' ')

#start

print("--- Welcome to HANGMAN game! ---\n\n")
print(f"The category is... {category.upper()}! Try to guess the word below...\n")
alive = True
lives = 0

while alive:
    if lives > 5:
        print(f"\n\nThe word was {word}.")
        print("The hangman died, you lost!")
        alive = False
    else:
        print(f"{' '.join(sub_list)}")
        guess = input("Type a letter ").upper()
        if guess not in word:
            print(man[lives])
            lives +=1
        else:
            for i in range(len(word)):
                letter = word[i]
                if guess == letter:
                    sub_list[i] = letter
            if "_" in sub_list:
                pass
            else:
                print(f"\n\nThe word is {word}.\n")
                print("Congratulation, you win!")
                break
