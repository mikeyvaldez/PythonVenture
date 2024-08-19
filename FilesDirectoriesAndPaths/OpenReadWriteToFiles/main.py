#!/usr/bin/env python3


###############################################################
# This is one way to read a file.

# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()    # need to close the file to free-up computer resources
##############################################################

##############################################################
# This is another way to open and read a file without having to use .close()

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
##############################################################
# This is how to write to a file. Technically overwritting the text already in the file.

# with open("my_file.txt", mode="w") as file:    # mode="w" <-- stands for write.
#     file.write("New text.")

##############################################################
# This is how to write to a file. Adding to the original content in the file.
# with open("my_file.txt", mode="a") as file:      # mode="a" <-- stands for append.
#     file.write("\nNew text.")

##############################################################

##############################################################
# This is how to create a file and write to it.
with open("new_file.txt", mode="w") as file:
    file.write("New text.")