"""
Class: Introduction to Programming
Name: Sanjana Gupta
Date: 10/31/2017
many_things.py
=====

Create a turtle or processing program that draws multiple objects (with or
without animation) that uses a list of dictionaries to define the properties
of each object in your drawing. 

For example, in the stars exercise in class, we used a dictionary containing
x, y and v as keys that determined a star's position and velocity.
"""

#Drawing fireworks in random places in the sky

import turtle
import random
t = turtle.Turtle()
window = turtle.Screen()
window.setup(800, 800)
window.bgcolor("black")
t.hideturtle()
window.tracer(0)


#Generate random positions for a given number of fireworks
#Store them in a dictionary
def position(number_of_fireworks):
    positions = {}
    count = 0
    for i in range (number_of_fireworks):
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        positions[count] = (x, y)
        count += 1
    return positions

#Pick a color by randomly choosing a number
#Number corresponds to color in a dictionary
def pen_color():
    colors = {1: "red", 2: "yellow", 3: "orange", 4: "pink"}
    color_number = random.randint(1, 4)
    color_string = colors.get(color_number)

 #  Could also do:
 #  color_string = random.choice(colors)
 
    return color_string

#Randomly decide size of firework
def size():
    size = random.randint(5, 150)
    return size

#Randomly decide number of fireworks
def number_of_fireworks():
    number_of_fireworks = random.randint(5, 50)
    return number_of_fireworks

#Constantly draw and redraw fireworks
#Note: This doesn't stop, it's on an endless loop
def light_up_my_sky():
    t.clear()
    num_of_fireworks = number_of_fireworks()
    positions = position(num_of_fireworks)
    for i in range(num_of_fireworks):
        t.up()
        t.goto(positions.get(i))
        t.down()
        length = size()
        for j in range(20):
            if j % 5 == 0:
                t.color(pen_color())
            t.fd(length)
            t.rt(162)
        window.update()
    window.ontimer(light_up_my_sky, 1000)

    
light_up_my_sky()


window.mainloop()
