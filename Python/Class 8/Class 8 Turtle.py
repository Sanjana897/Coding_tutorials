#Class 8 Turtle

import turtle
t = turtle.Turtle()
window = turtle.Screen()
t.hideturtle()
window.tracer(0)
window.setup(400, 400)
window.bgcolor('black')
t.color('yellow')
t.pensize(5)

#Tuples in lists
"""
for x, y in [(0,50),(50,50),(50,0),(0,0)]:
    t.goto(x, y)
"""

#Draw a single star
def draw_star(x, y, s):
    t.setheading(0)
    t.up()
    t.goto(x, y)
    t.down()
    for i in range(5):
        t.left(144)
        t.forward(s)

velocity = 4
pos = [100, 100]

def draw():
    global velocity #To alter the variable within the function
    t.clear()
    pos[1] -= velocity #Change the y position to subtract 50
    x, y = pos #Multiple assignment using tuples
    draw_star(x, y, 50) 

    window.update() #Refresh the screen
    if pos[1] <= -200: #When it hits the bottom
        velocity *= -1 #The velocity gets reversed (multiply by -1)
    window.ontimer(draw, 50) #1/2 second later, run this same function again

draw()

window.mainloop()
