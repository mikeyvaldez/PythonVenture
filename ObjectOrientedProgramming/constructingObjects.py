#!/usr/bin/env python3

# here 'turtle' the module, 'Turtle' is the class
from turtle import Screen, Turtle     
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("blue")

my_screen = Screen()
print(my_screen.screensize(canvwidth=10, canvheight=10))
my_screen.exitonclick()