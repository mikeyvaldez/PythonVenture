#!/usr/bin/env python3


# an Attribute is a variable that is associated with an object
# The contructor initializes attributes..

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0

user_1 = User("001", "Mike")
user_2 = User("002", "Bere")

print(user_1.followers)