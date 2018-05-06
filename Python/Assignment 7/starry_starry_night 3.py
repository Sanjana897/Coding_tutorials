"""
starry_starry_night.py
=====
Draw some stars! See instructions in site under homework 7t stat

"""

import turtle
import random

window = turtle.Screen()
t = turtle.Turtle()

window.setup(800, 600)
#t.hideturtle()
#window.tracer(0)
window.bgcolor("dark blue")
t.color("yellow")
t.pensize(3)


def finding_center_x(x, y, side): 
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.forward(side)
    t.left(72)
    t.forward(side)
    xcoordinate = t.xcor()
    return xcoordinate

def center_to_point(x, y, side):
    centre_x = finding_center_x(x, y, side)
    distance = centre_x - x
    return distance

def draw_star(x, y, side):
    distance = center_to_point(x, y, side)
    go_up = distance - side
    t.penup()
    t.goto(x, y + go_up)
    t.setheading(0)
    t.back(distance)
    t.pendown()
    for i in range (5):
        t.forward(side)
        t.left(72)
        t.forward(side)
        t.right(144)
    window.update() #Has to be commented out for optional part to work
draw_star(0, 0, 100)    
    
#Part 1: Drawing star in the center of the screen
#Managed to get the x-coordinate centered, using finding_center_x and center_to_point
"""
draw_star(-131, 50, 100)
"""

#Part 2.1: Drawing stars in a line
"""
x = -390
y = 200
side = 10
for i in range(1000):
    draw_star(x, y, side)
    midpoint = center_to_point(x, y, side)
    x += (2*midpoint)
    window.update()
"""

#Part 2.2: Drawing stars in a line
#Used an exponent to get the curve
"""
x = -390
y = -270
side = 10
for i in range(10):
    draw_star(x, y, side)
    x += i**2.5
    y += 70
    side += 3
"""   

#Part 3: Generate star data
"""
def generate_star_data(number_of_stars):
    star_data = []
    for i in range(number_of_stars):
        star = []
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        size = random.randint(1, 50)
        velocity = random.randint(1, 5)
        star.append(x)
        star.append(y)
        star.append(size)
        star.append(velocity)
        star_data.append(star)
    return star_data
"""

#Part 4: Drawing the sky
"""
star_data = generate_star_data(40)

def draw_sky():
    for i in star_data:
        x = i[0] 
        y = i[1]
        side = i[2]
        draw_star(x, y, side)

draw_sky()
"""

#Part 5: Optional
"""
I got Ben's help with this part because I followed the instructions
but it wasn't working for me.
"""

"""
star_data = generate_star_data(40)

def draw_sky():
    t.clear()
    for i in range(len(star_data)):
        star_data[i][0] += star_data[i][3]
        x = star_data[i][0]
        y = star_data[i][1]
        side = star_data[i][2]
        draw_star(x, y, side)
    window.ontimer(draw_sky, 30)
    window.update()


draw_sky()
"""

    

window.mainloop()
