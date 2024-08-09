#!/usr/bin/env python3

from art import logo, vs
from game_data import data
import random


def format_data(account):
    # Takes the account data and returns printable format.
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    # Take a user's guess and the follower counts and returns if they got it right.
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Display art
print(logo)
score = 0
game_Continue = True
account_b = random.choice(data)

while game_Continue:
    # Generate a random account from the game data

    # Making account at position B become the next account position A.
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:   # if the element that is randomly chosen is the same, randomize account b until it is a different element
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")


    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen
    print("\n" * 20)
    print(logo)

    # Check if user is correct.
    ##  Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess.    
    if is_correct:
        score += 1     # score keeping.
        print(f"You're right! Current score {score}")
    else:
        print(f"You're wrong... {score}.")
        game_Continue = False     # Make the game repeatable.
    
    
    












