#!/usr/bin/env python3


# --------------------------
# The following code will cause a type error because
# you cannot concatenate an integer with a string

# num_char = len(input("What is your name? "))
# print("Your name has " + num_char + " characters.")

# --------------------------


# --------------------------
# The following code uses the type() function

# num_char = len(input("What is your name? "))
# print(type(num_char))
# --------------------------



# --------------------------
# The following code displays Type Conversion
# 

# num_char = len(input("What is your name? "))

# new_num_char = str(num_char)

# print("Your name has " + new_num_char + " characters.")


a = float(123)
print(type(a))

print(70 + float("100.5"))

print("60" + "100")

# --------------------------