#!/usr/bin/env python3

# List comprehension cuts down on the amount of typing and
# makes code a lot shorter and easier to read.
# List Comprehension: is a case where you create an new list
# from a previous list


######################################################################################
# examples of list comprehension
numbers = [1,2,3]
new_numbers = [n + 1 for n in numbers]    # an example of list comprehension
print(new_numbers)


name = "Michael"
letters_list = [letter for letter in name]   # creates a list from the the string
print(letters_list)



new_list = [n * 2 for n in range(1, 5)]
print(new_list)
######################################################################################

######################################################################################
# Conditional List Comprehension
# key word pattern [new_item for item in list if test]

names = ["Henry", "Alex", "Lorenzo", "Beth", "Dave", "Ellouise", "Freddison"]
short_names = [name for name in names if len(name) < 5]
capital_names = [name.upper() for name in names if len(name) > 5]
print(short_names)
print(capital_names)


######################################################################################