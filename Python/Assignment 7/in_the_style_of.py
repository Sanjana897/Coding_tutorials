"""
Class: Introduction to Programming
Name: Sanjana Gupta
Date: 10/21/2017
in_the_style_of.py
=====
Create a drawing/sketch in the style of some visual art that you like. For
example, you can try making a sketch that looks like a Piet Mondrian
painting, or you can experiment with Truchet tiles! This is pretty freeform,
so there are no other requirements!
"""

import turtle
import random

window = turtle.Screen()
t = turtle.Turtle()
window.setup(700, 700)
window.bgcolor("black")

t.hideturtle()
window.tracer(0)

###Drew two things, one is a spiral
###Uncomment one on the other to view
"""
def spiral():
    for i in range (90):
        t.circle(100)
        if i <= 30:
            t.color("green")
        if i > 30 and i <= 60:
            t.color("blue")
        if i > 60 and i <= 90:
            t.color("purple")
        t.right(5)
    window.update()
spiral()
"""

###Second is an animation, to get a hang of ontimer

"""
#This is one of the two triangles that makes up the pattern
def bottom_triangle(current_x, current_y):
    t.goto(current_x, current_y - 70)
    t.goto(current_x + 70, current_y - 70)
    t.goto(current_x, current_y)
    
#This is the other of the two triangles that makes up the pattern   
def upper_triangle(current_x, current_y):
    t.goto(current_x + 70, current_y)
    t.goto(current_x + 70, current_y - 70)
    t.goto(current_x, current_y)

#Selects black and white randomly
def choose_color():
    response = random.randint(1, 2)
    if response == 1:
        colour = "white"
    else:
        colour = "black"
    return colour

        
#Repeats tiles in a pattern across and then down in a for loop
#Calls on color function before drawing each tile, so color changes
#Looked up documentation for begin and end fill
def tiles():
    starting_x = -350
    starting_y = 350
    for j in range (11):
        for i in range(10):
            t.up()
            t.goto(starting_x, starting_y)
            t.down()
            t.color(choose_color())
            t.begin_fill()
            bottom_triangle(starting_x, starting_y)
            t.end_fill()
            t.begin_fill()
            upper_triangle(starting_x, starting_y)
            t.end_fill()
            starting_x = starting_x + 70
        starting_x = -350
        starting_y = 350 - (j * 70)
        t.up()
        t.goto(starting_x, starting_y)
        t.down()
    window.update()

tiles()
window.ontimer(tiles, 2000)
window.ontimer(tiles, 4000)
window.ontimer(tiles, 6000)
window.ontimer(tiles, 8000)
window.ontimer(tiles, 10000)
window.ontimer(tiles, 12000)
window.ontimer(tiles, 14000)
window.ontimer(tiles, 16000)
"""
    
    












window.mainloop()
