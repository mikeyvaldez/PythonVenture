#!/usr/bin/env python3



import pandas     # type: ignore

data = pandas.read_csv("weather_data.csv") # data is considered a pandas dataframe object
# print(data["temp"])     # this here is known as a pandas series object

# data_dict = data.to_dict()    # turns the data into a dictionary
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)


##############################################
# getting the average with a for loop
# sum = 0
# for temp in temp_list:
#     sum += temp

# average = sum // len(temp_list)
# print(average)
#############################################

############################################
# getting the average using sum() and len() methods
# average = sum(temp_list) / len(temp_list)
# print(average)
###########################################

##########################################
# using the pandas Series.mean() or data series method
# print(data["temp"].mean())
##########################################

##########################################
# using the pandas series method max() to get the maximum value in the list.
# print(data["temp"].max())
###########################################

###############################################
# Get Data in Column
# These lines of code show us that pandas takes the columns and turns them into attributes.
# The second line shows condition used as a valid attribute.
# print(data["condition"])
# print(data.condition)
###############################################

###############################################
# How to get data in a Row
# data[data["day"]]
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
###############################################

###############################################
# How to convert from celsius to farenheit
# formula:    (0^C * 9/5) + 32 = 32^F

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(f"{monday_temp_F}^F")

###############################################
# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
# the bottom line of code creates a new csv file and adds the data from the created dictionary
# using the to_csv() method in from pandas
data.to_csv("new_data.csv") 