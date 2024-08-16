#!/usr/bin/env python3

from turtle import Turtle

class Paddle(Turtle):  # inherit from the Turtle class

    def __init__(self, position):
        # Initializing the super class will give you all abilities, methods, and attributes from the Turtle class
        super().__init__()
    
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)


    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

