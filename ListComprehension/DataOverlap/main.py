#!/usr/bin/env python3



with open("file1.txt", mode="r")as file1:
    file_one_content = file1.readlines()
    
with open("file2.txt", mode="r") as file2:
    file_two_content = file2.readlines()

clean_list_one = [fileOne.strip() for fileOne in file_one_content]
clean_list_two = [fileTwo.strip() for fileTwo in file_two_content]

result = [int(item) for item in clean_list_one if item in clean_list_two]

print(result)