#!/usr/bin/env python3




# Simple Function
def greet():
    print("What's up Mikey Mike")
    print("How have you been?")
    print("Keep grinding out code!\n")

greet()


# Function that allows for input
# Remember the difference between a parameter and an argument.
# a parameter is what goes in the parenthesis at the beginning of a function.
# An argument is the data that the parameter is holding


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Mike")