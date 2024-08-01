#!/usr/bin/env python3

# A prime number can only be divisible by 1 and itself

print("Enter number to check if it is a prime number:")
n = int(input())   # Check This number

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's NOT a prime number.")


prime_checker(number = n)