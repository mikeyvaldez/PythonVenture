#!/usr/bin/env python3

# The following code is one of many ways to determine whether 
# a year is a leap year.


# Which year do you want to check?
year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not Leap Year")        
    else:
        print("Leap year")
else:
    print("Not leap year")
