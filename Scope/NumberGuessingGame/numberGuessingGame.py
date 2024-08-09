#!/usr/bin/env python3


from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

# Function to check users' guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    # Checks answer against guess, returns the number of turns remianing.
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    # Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Psst, the correct answer is {answer}")


    turns = set_difficulty()


    guess =  0
    # Repeat the guessing functionality if theyget it wrong
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let user guess a number
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()



























# magic_number = 87

# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")

# difficulty_option = input("Type 'easy' or 'hard': ")

# easy_tries = 5
# hard_tries = 10

# if difficulty_option == 'easy':
#     user_easy_guess = int(input("What is your first guess? "))

#     while easy_tries > 5:
#         print("You have {} tries left".format(easy_tries))
#         if user_easy_guess == magic_number:
#             print("You got it!")
#         elif user_easy_guess < magic_number:
#             print("Guess Higher!")
#             easy_tries -= 1
#         elif user_easy_guess > magic_number:
#             print("Guess Lower!")
#             easy_tries -= 1
        
