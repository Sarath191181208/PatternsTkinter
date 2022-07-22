# import colorsys

# turtle.pencolor('SpringGreen2')

# c = colorsys.hsv_to_rgb(h, 0.7, 0.7


import turtle
import random 
import colorsys
from math import pi, sin, cos

turtle.pensize(20)
turtle.speed(10)

def draw_circle(r):
	turtle.up()
	turtle.setposition(r, 0)
	turtle.down()

	for angle in range(360):
		c = colorsys.hsv_to_rgb(angle/360, 1, 1)
		turtle.pencolor(c)
		# rgb 
		a = (pi / 180) * angle
		x = r * cos(a)
		y = r * sin(a)

		turtle.goto(x, y)


turtle.bgcolor("#000")

turtle.pencolor("SpringGreen2")
# turtle.circle(10)
draw_circle(10)

shape_size = 10
k = 3/ 4
turtle.up()


for i in range(1, 4*360):
	c = colorsys.hsv_to_rgb(i/360, 0.5, 0.7)
	turtle.pencolor(c)
	a = i  * (pi/ 180)
	A = 10;
	r = shape_size * A * cos(k * a);
	x = r * cos(a);
	y = r * sin(a);

	turtle.goto(x, y)
	turtle.down()

turtle.mainloop()