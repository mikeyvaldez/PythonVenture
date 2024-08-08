#!/usr/bin/env python3



# Python does not have block scope


# This means that variables created nesed in other blocks of code e.g. for loops, if statements,
# while loops etc. dont' get local scope. They are given function scope if they are within a
# function or global scope if they are not.


game_level = 10
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)