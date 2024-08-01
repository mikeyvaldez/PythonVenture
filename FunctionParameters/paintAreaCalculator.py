#!/usr/bin/env python3

import math


test_h = int(input())   # Height of wall (m)
test_w = int(input())     # Width of wall  (m)
coverage = 5


def paint_calc(height, width, cover):
    num_cans = (height * width) / cover
    round_up_cans = math.ceil(num_cans)
    print(f"You'll need {round_up_cans} cans of paint.")


# call the function
paint_calc(height = test_h, width = test_w, cover = coverage)