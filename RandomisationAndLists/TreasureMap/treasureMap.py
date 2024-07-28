#!/usr/bin/env python3

# This program will mark a spot on a map with an X
# This map contains a nested list. When map is printed this is what it looks like, notice the nesting
# [['', '', ''], ['', '', ''], ['', '', '']]

line1 = ["", "", ""]
line2 = ["", "", ""]
line3 = ["", "", ""]
map = [line1, line2, line3]
print("Hiding your treasure! x marks the spot.")
position = input()   # Where do you want to put the treasure?

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "x"


print(f"{line1}\n{line2}\n{line3}")