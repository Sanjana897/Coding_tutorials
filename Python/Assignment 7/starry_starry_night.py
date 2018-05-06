"""
starry_starry_night.py
=====
Draw some stars! See instructions in site under homework 7t stat

"""

import turtle
import random

#Setting up the file
window = turtle.Screen()
t = turtle.Turtle()
window.setup(800, 600)
t.hideturtle()
window.tracer(0)
window.bgcolor("dark blue")
t.color("yellow")
t.pensize(3)

def draw_star(x, y, side):
    t.up()
    t.goto(x, y)
    t.down()
    for i in range (5):
        t.forward(side)
        t.left(72)
        t.forward(side)
        t.right(144)
    window.update()
    
#Part 1: Drawing star in the center of the screen
"""
Note: I haven't calculated the exact center, I approximated it visually.
Because I assigned side to be length of each arm of the star, so it's hard to
calculate the total length of the star across without some trigonometry, which
I'm not sure is required/worthwhile.
"""
"""
draw_star(-131, 50, 100)
"""

#Part 2: Drawing stars in a line
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
def generate_star_data(number_of_stars):
    star_data = []
    for i in range(number_of_stars):
        star = []
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        size = random.randint(1, 50)
        star.append(x)
        star.append(y)
        star.append(size)
        star_data.append(star)
    return star_data
        
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
I followed the instructions but this part isn't working for me.
"""

star_data = generate_star_data(40)

def draw_sky():
    for i in star_data:
        x = i[0] + 1 
        y = i[1]
        side = i[2]
        draw_star(x, y, side)
    window.ontimer(draw_sky, 30)

draw_sky()


    



window.mainloop()
