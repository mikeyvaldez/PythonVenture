#!/usr/bin/env python3



def is_leap_year(year):
    return (year % 4 == 0 and year % 100 == 0) or (year % 400 == 0)


print(is_leap_year(2025))