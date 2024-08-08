#!/usr/bin/env python3


# Prime numbers are numbers that can only be cleanly divided by themselves and 1
#  write a function called is_prime() that checks whether if the 
# number passed into it is a prime number or not.  It should return True or False.
number = int(input("Enter number to check if it is a prime number: \n"))

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(number))