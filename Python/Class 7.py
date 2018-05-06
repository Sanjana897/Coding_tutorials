#Class 7 
#Turtle

import turtle
import random

#Setting up the screen as the canvas
window = turtle.Screen()

#Setting up window. If you don't specify, default is 50% and 75% of screen
#Default background is white, if you don't specify this
#window.setup(400,400) #width, height
#window.bgcolor("green")

#Naming our turtle
t = turtle.Turtle()

#Color and pensize. Note that color is a string. Pensize is an integer
#Default color is black, pensize is 1
t.color("blue")
t.pensize(5)

#Hides the arrow on the line
#t.hideturtle()

#Sets tracer speed to fastest possible
#window.tracer(0)

#Draws an S
#Movement: forward and back, distance specified
#Direction: right and left, angle specified
"""
t.back(75)
t.right(90)
t.forward(50)
t.left(90)
t.forward(100)
t.right(90)
t.forward(70)
t.right(90)
t.forward(100)
"""

#Using up and down to draw interrupted lines
"""
t.left(90)
t.forward(40)
t.up()             # don't draw
t.forward(20)
t.down()           # draw
t.forward(40)
t.up()             # don't draw
t.forward(20)
t.down()           # draw
t.forward(40)
t.left(90)
t.forward(40)
t.up()             # don't draw
t.forward(20)
t.down()           # draw
t.forward(40)
t.up()             # don't draw
t.forward(20)
t.down()           # draw
t.forward(40)
"""

#goto for diagnols
"""
t.goto(200, 200)
"""

#Drawing a house with goto
"""
t.goto(-100, 0)
t.goto(-100, 100)
t.goto(-50, 150)
t.goto(0, 100)
t.goto(0, 0)
"""

#Using random to change pensize, goto coordinates
"""
for i in range(50):
    t.pensize(random.randint(1, 12))
    t.goto(random.randint(-300, 300), random.randint(-200, 200))
    if i == 25:
        # change the color once to green
        t.color("purple")
"""

#Drawing a square with goto
"""
t.goto(200,0)
t.goto(200,200)
t.goto(0,200)
t.goto(0,0)
"""

#Drawing a square with forward and left
"""
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
"""

#Using a function to draw a square instead of manually typing code
"""
def square: 
    for i in range (4):
        t.forward(200)
        t.left(90)
"""

#Function to draw a pentagon
#Parameters: x,y co-ordinates for start point and size of each side
#Picks up pen, goes to start point, puts down and starts drawing there
#Interior angle of polygon = 360/number of sides
#So 90 for square or rectangle, 72 for pentagon
"""
def pentagon(x, y, size):
    t.up()
    t.goto(x, y)
    t.down()
    for i in range(5):
        t.forward(size)
        t.left(72)
        
pentagon(0, 0, 200)
"""

#So can do generic function for any sided-shape
#Parameters include number of sides
"""
def polygon(x, y, size, sides):
    angle = 360 / sides
    t.up()
    t.goto(x, y)
    t.down()
    for i in range(sides):
        t.forward(size)
        t.left(angle)

polygon(0, 0, 100, 8)
"""

#Calling the polygon function 100 times in a row
"""
for i in range(3, 100):
    polygon(0, 0, 50, i)
"""

#A square that can be positioned anywhere as opposed to drawn at starting point
#Spirograph
"""
def moving_square(x, y, size):
    t.up()
    t.goto(x, y)
    t.down()
    for i in range(4):
        t.forward(size)
        t.left(90)

#Spirograph!!
for i in range(1000):
    t.left(15) #angle is changed on each iteration
    moving_square(i * 2, 0, 100) #x coordinate is moved
    #wn.update() #Updates window so that it's fully drawn, don't have to watch each one
"""

#circle with circle(radius)
"""
t.circle(50)
"""

#Using ontimer
#Calls drawsquare in 2, 4, 6 and 8 seconds
#Note: Time is in milliseconds
def draw_square(size):
    t.hideturtle()
    for i in range(4):
        t.forward(size)
        t.left(90)
"""
def draw_stuff():
    draw_square(20)
    t.up()
    t.forward(22)
    t.down()
    window.update()

window.ontimer(draw_stuff, 2000)
window.ontimer(draw_stuff, 4000)
window.ontimer(draw_stuff, 6000)
window.ontimer(draw_stuff, 8000)
"""

#Same draw stuff function, but timer is moved into function body
#and function is called once outside of it
#Function now gets called again every half second, endless loop
"""
def draw_stuff():
    draw_square(20)
    t.up()
    t.forward(22)
    t.down()
    window.update()
    window.ontimer(draw_stuff, 500)

draw_stuff()
"""

#Clear one square before drawing the next, making it look like animation
"""
def draw_stuff():
    # clear the screen
    t.clear()
    draw_square(20)
    t.up()

    # descrease the forward movement 
    t.forward(22)
    t.down()
    window.update()
    window.ontimer(draw_stuff, 500)

draw_stuff()
"""

#Bouncing ball animation
"""
turtle_x, turtle_y, turtle_dx, turtle_dy = [0], [0], [0], [-0.1]

#  store acceleration
acc = -0.5

#  turn animation of turtles off
window.tracer(0)
t.hideturtle()

#  draw function goes here
def draw():
    t.clear()
    t.penup()
    t.goto(turtle_x[0], turtle_y[0])
    t.pendown()
    turtle_y[0] += turtle_dy[0]

    # change velocity based on acceleration
    turtle_dy[0] += acc
    t.circle(15)

    window.update()
    window.ontimer(draw, 30)
    
    # bounce!
    if turtle_y[0] <= -250:
        turtle_dy[0] *= -1

draw()
"""

#Have to have this at the bottom to start the program
window.mainloop()
