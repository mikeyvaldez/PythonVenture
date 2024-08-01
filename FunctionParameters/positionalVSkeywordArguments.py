#!/usr/bin/env python3


# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")

#greet_with("Mike", "Wisconsin")  # these are positional arguments, position matters. or program may not make sense or may not function properly.

greet_with(name = "Michael", location = "Salinas") # With keyword arguments, you can switch the order of them around and it would function the same
# greet_with(location = "Salinas", name = "Michael") # this shows the order doesnt matter regarding keyword arguments.

