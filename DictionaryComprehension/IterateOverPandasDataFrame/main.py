#!/usr/bin/env python3

import pandas


student_dict = {
    "student": ["Michael", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)


student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)


# Loop through a data frame
# for (key, value) in student_data_frame.items():
#     # print(key)
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)   # each row is a pandas series object
    # print(row.student)
    # print(row.score)
    if row.student == "Michael":
        print(row.score)