#!/usr/bin/env python3

import random
from hangmanWordList import word_list
from hangmanArt import logo
from hangmanArt import stages

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Set lives to 6
lives = 6

print(logo)

# Line for Testing code
print(f'Psst, the solution is {chosen_word}')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"


while not end_of_game:
    guess = input("Gues a letter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter        

    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You Win!")
    
    # Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
