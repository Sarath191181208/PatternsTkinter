import turtle
from math import pi, cos, sin 

turtle.bgcolor("#000")
turtle.pencolor("SpringGreen2")
turtle.pensize(5)
turtle.speed(10)
turtle.up()

peak_size = 50
x = 0
epicycles = 100

# y(3) = 0.2
# y(11) = 0.05
# 3 -> 0.2 
# 11 -> 0.05

# spread = 0.2 + (0.45/8) - (epicycles*0.15/160)
spread = 0.01

for i in range(360):
	t = (pi/ 180)*i 

	# x = 0
	y = 0 
	for i in range(epicycles):
		k = (i*2) +1
		r = (4*sin(k*t))/ (k*pi)
		y += r

	x += spread*i 
	y *= peak_size

	turtle.goto(x, y)
	turtle.down()

turtle.mainloop()