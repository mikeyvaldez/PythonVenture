#!/usr/bin/env python3


def add(n1, n2):
    return n1 + n2

my_favourite_operation = add     # This is how you assign a function to variable without calling the function. Without the parenthesis

print(my_favourite_operation(2, 3))     # You then use the parenthesis with newly created variable