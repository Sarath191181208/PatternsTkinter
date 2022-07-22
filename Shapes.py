import turtle
from math import pi, cos, sin

turtle.pencolor("SpringGreen2")
turtle.fillcolor("#0f0")
# turtle.begin_fill()

# Rose curves
# k = n/ d
# r=a cos(k\θ)

# x = r cos(θ)
# y = r sin(θ)
turtle.bgcolor("#383838")
turtle.pensize(5)
turtle.speed(20)
turtle.up()

shape_size = 10

for i in range(1, 4*360):
	a = i * (pi/ 180)

	# x = cos(a) (6sin(a) ^ 2)
	x = cos(a) * pow((sin(a) * 6), 2)
	y = sin(a) * pow((-cos(a) * 6), 2)

	x *= shape_size;
	y *= shape_size;

	turtle.goto(x, y)
	turtle.down()

# turtle.end_fill()

turtle.mainloop()