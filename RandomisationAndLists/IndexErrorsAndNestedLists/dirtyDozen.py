#!/usr/bin/env python3




#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peahces", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# This causes an index Error because it is trying to access the 8th index
# indexes start from 0 and on 0-10 for ex.
#print(fruits[7])

# Nested List (a list that contains two lists)
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# how to access the nested list
print(dirty_dozen[0][1])
print(dirty_dozen[1][1])