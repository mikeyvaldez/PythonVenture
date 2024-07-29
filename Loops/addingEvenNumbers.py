#!/usr/bin/env python3


target = int(input())    # Enter a number between 0 and 100


# even_sum = 0
# for number in range(2, target + 1, 2):
#     # accumulate even_sum here
#     even_sum += number
# print(even_sum)


# or

alternative_sum = 0
for number in range(1, target + 1):
    if number % 2 == 0:
        alternative_sum += number
print(alternative_sum)