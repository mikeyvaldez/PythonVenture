#!/usr/bin/env python3

# Which number do you want to check?
number = int(input())

# If the number can be divided by 2 with 0 remainder.
if number % 2 == 0:
    print("This is an even number.")
# Otherwise (number cannot be divided by 2 with 0 remainder)l
else:
    print("This is an odd number.")