#!/usr/bin/env python3


# *args: Many Positional Arguments
# turns all the arguments into a tuple


def add(*args):
    print(args[0])

    sum = 0
    for n in args:
        sum += n
    return sum



print(add(3, 5, 6))