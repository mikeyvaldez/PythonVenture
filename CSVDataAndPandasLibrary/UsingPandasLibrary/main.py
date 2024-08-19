#!/usr/bin/env python3



import pandas     # type: ignore

data = pandas.read_csv("weather_data.csv") # data is considered a pandas dataframe object
# print(data["temp"])     # this here is known as a pandas series object

data_dict = data.to_dict()    # turns the data into a dictionary
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)


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
average = sum(temp_list) / len(temp_list)
print(average)
###########################################

##########################################
# using the pandas Series.mean() or data series method
print(data["temp"].mean())
##########################################