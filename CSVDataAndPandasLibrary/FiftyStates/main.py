#!/usr/bin/env python3


import turtle
import pandas    # type: ignore

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State",
                                    prompt="What's another state's name?").title()
    


    if answer_state in all_states:     # If answer_state is one of the states in all the states of the 50_states.csv    
        guessed_states.append(answer_state)
        t = turtle.Turtle()     # Create a turtle to write the name of the state at the state's x and y coordinate
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.item()), int(state_data.y.item()))    
        t.write(answer_state)
        


screen.exitonclick()






# screen.exitonclick()