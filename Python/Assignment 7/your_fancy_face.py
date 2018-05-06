"""
your_fancy_face.py 
=====
Draw a face using turtle. For example, you can draw the look of disapproval!

![look of disapproval](https://foureyes.github.io/csci-ga.1120-fall2017-001/resources/img/turtle/your_face.png)

Requirements
-----

* you can draw whatever face you like
* but you have to use the turtle module
    * change the size of the pen 
    * set the window size to 400 x 400
    * turn animation off (for sanity's sake)
* your face should
    * use at least one circle
    * use at least one line

"""
import turtle

window = turtle.Screen()
t = turtle.Turtle()
window.setup(400, 400)
window.tracer(0)
t.hideturtle()

def draw_circle(x, y, radius, fill_color):
    t.up()
    t.goto(x, y)
    t.down()
    t.fillcolor(fill_color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

#Drawing the first ear
draw_circle(40, 70, 15, "black")

#Drawing the second ear
draw_circle(-40, 70, 15, "black")

#Drawing the main face
draw_circle(0, 0, 50, "white")

#Drawing one black eye
draw_circle(18, 45, 15, "black")

#Drawing the second black eye
draw_circle(-18, 45, 15, "black")

#Drawing the first cornea
draw_circle(16, 54, 8, "white")

#Drawing the second cornea
draw_circle(-16, 54, 8, "white")

#Drawing the first eyeball
draw_circle(17, 58, 2, "black")

#Drawing the second eyeball
draw_circle(-17, 58, 2, "black")

#Drawing the nose
draw_circle(0, 30, 5, "black")

#Drawing the line between the nose and the mouth
t.up()
t.goto(0, 30)
t.down()
t.right(90)
t.forward(5)

#Drawing the mouth, using two arcs
#Documentation: turtle.circle(radius, extent=None, steps=None)
t.circle(8, 180)
t.up()
t.goto(0, 25)
t.down()
t.circle(8, -180)

window.update()
window.mainloop()

