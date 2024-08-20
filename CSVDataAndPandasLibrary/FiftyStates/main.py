#!/usr/bin/env python3


import turtle

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?r")
print(answer_state)

# screen.exitonclick()