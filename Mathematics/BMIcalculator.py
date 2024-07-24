#!/usr/bin/env python3

# The BMI is a measure of someone's weight taking into account
# their height. e.g. If a tall person and a short person both weigh the
# same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the
# square of their height (in m):

# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()


weight_as_int = int(weight)
height_as_float = float(height)

# Use the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or you can use multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

# prints the solution as float
print("Solution as a decimal: ") 
print(bmi)

print(" ")

# rounds the solution up
bmi_as_int = int(bmi)
print("Solution as an integer: ")
print(bmi_as_int)
