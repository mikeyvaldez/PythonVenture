#!/usr/bin/env python3

# Take a users height and weight then calculate the bmi
# and we are going to output a print statement telling them 
# the bmi that was calculated then give them an interpretation

# Enter your height in meters e.g.., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())

# bmi formula is weight mulitplied by height squared
bmi = weight / (height * height)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
