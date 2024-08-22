#!/usr/bin/env python3



sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list_of_words = sentence.split()

result = {word:len(word) for word in list_of_words}


print(result)