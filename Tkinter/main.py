#!/usr/bin/env python3


import tkinter



window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)



# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()    # need the .pack() method for the label to appear on the screen








window.mainloop()    # mainloop() keeps the gui open, basically a while loop