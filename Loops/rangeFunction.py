#!/usr/bin/env python3


# For loop with range function
# for number in range(1, 11):   # range is from 1 - 11 not including 11 so prints 1 - 10
#     print(number)


# for number in range(1, 11, 3):   # range is from 1 - 11 not including 11 so prints 1 - 10 but in steps of 3
#     print(number)


# this for loop adds all the numbers up from 1 - 100
total = 0
for number in range(1, 101):
    total += number
print(total)