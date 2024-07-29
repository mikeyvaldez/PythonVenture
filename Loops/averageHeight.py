#!/usr/bin/env python3

# This program takes in integers separated by a space
# takes those numbers and stores them in a list.
# It then takes the values in list and adds them all together.
# It also counts the number of students.
# It also calculates the average height.


# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])


# Adds all the heights of the students together and prints the total value
total_height = 0
for height in student_heights:
    total_height += height
print(f"total height = {total_height}")

# Adds the number of students together and prints total amount of students
number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"number of students = {number_of_students}")

# Calculates the average height out of all the students in the list
average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")