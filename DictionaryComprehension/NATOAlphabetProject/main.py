#!/usr/bin/env python3


import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)