import random
from word_list import word_list
lives = 6
correct_letters = []
take_the_word = random.choice(word_list)
print(take_the_word)

placeholder = ""
for i in range(len(take_the_word)):
    placeholder += "_"
print(placeholder)

game_over = False
while not game_over:
    take_letter = input("Guess the Letter: ").lower()
    if take_letter in correct_letters:
        print("You already used it")
    display = ""

    for letter in take_the_word:
        if letter == take_letter:
            display += letter
            correct_letters.append(take_letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"



    print(display)

    if take_letter not in take_the_word:
        lives -= 1
        print(f"You have {lives} left")
        if lives ==0:
            game_over = True
            print("You Lose")

    if "_" not in display:
        game_over = True
        print("You Win")

