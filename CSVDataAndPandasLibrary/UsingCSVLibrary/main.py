#!/usr/bin/env python3


import csv      # <-- the csv reading and writing library

# with open("weather_data.csv") as weather_data_file:    # displays weather data as a list
#     data = weather_data_file.readlines()
#     print(data)



with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)     # this line creates a csv.reader object
    temperatures = []
    for row in data:     # we then loop through the csv data in this line
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)