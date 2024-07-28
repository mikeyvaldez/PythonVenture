#!/usr/bin/env python3


# List of states which joined the USA in chronological order

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Conneticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire",
                     "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennesse", "Ohio", "Lousiana", "Indiana", "Mississippi",
                     "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon",
                     "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
                     "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# printing things from a list
print(states_of_america[0]) # first item in the list "Delaware"
print(states_of_america[-1]) # last item in the list "Hawaii"

# change things in a list
states_of_america[1] = "Pencilvania"
print(states_of_america)
print("-------------------------")

# Add something to the list using append()
states_of_america.append("Michaelland")
print(states_of_america)
print("-------------------------")

# adding two lists together using extend()
states_of_america.extend(["Bereniceland", "Simone Blair Land"])
print(states_of_america)
