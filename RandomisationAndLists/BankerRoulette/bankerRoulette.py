#!/usr/bin/env python3

import random

names = ["Michael", "Henry", "Eric", "Lorenzo"]


# Get the total number of items in list.
num_items = len(names)

# Generate random numbers between 0 and the last index.
random_choice = random.randint(0, num_items - 1)

# Choose and print a random name.
print(names[random_choice])