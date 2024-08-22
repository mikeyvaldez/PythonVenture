#!/usr/bin/env python3


# *args: Many Positional Arguments
# turns all the arguments into a tuple


def add(*args):
    print(args[0])

    sum = 0
    for n in args:
        sum += n
    return sum



# print(add(3, 5, 6))
#################################################

# **kwargs: Many Keyword Arguments
# keyword arguments is basically a dictionary
# kwargs are keyword argument and their value

def calculate(n, **kwargs): # here n represents a positional argument, and **kwargs represents the rest of the keyword arguments
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)