#!/usr/bin/env python3


# This is the key word structure for looping through a dictionary
# {new_key:new_value for (key, value) in dictionary.items()}



import random

names = ["Henry", "Alex", "Lorenzo", "Beth", "Dave", "Ellouise", "Freddison"]

student_score = {student:random.randint(1, 100) for student in names}

passed_students = {student:score for (student, score) in student_score.items() if score >= 60}
print(passed_students)