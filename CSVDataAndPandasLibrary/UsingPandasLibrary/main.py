#!/usr/bin/env python3



import pandas     # type: ignore

data = pandas.read_csv("weather_data.csv")
print(data["temp"])