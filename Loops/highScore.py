#!/usr/bin/env python3

# This program takes integers separated by a space 
# puts those integers into a list and determines which 
# number is the highest


# Input a list of student scores
# grabs the input from the user and puts it into a list
student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])


# calculates the highest score
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
        # print(highest_score)

print(f"The highest score in the class is: {highest_score}")