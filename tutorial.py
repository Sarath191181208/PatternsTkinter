import turtle
from math import pi, cos, sin

# forward(dis)
# turtle.forward(300)

# back(dis)
# turtle.back(100)

# right(angle)
# turtle.right(90)

# left(angle)
# turtle.left(90)


## Sorthand notations
# - forward -> fd
# - backward -> bk
# - right -> rt
# - left -> lt

# turtle.goto(100, 100)

# x^2 + y^2 = r^2
# x = r cos(a)
# y = r sin(a)
# r = 30

# for angle in range(360):
#     # deg -> radians
#     angle_radians = (pi / 180) * angle
#     x = r * cos(angle_radians)
#     y = r * sin(angle_radians)

#     turtle.goto(x, y)

# turtle.circle(30)

# Problem
# Draw a square
side_length = 100
n = int(input("Enter the n sided polygon you want : "))
angle = 180 - ((n - 2) * 180) / n
# n sided polygon
for i in range(n):
    turtle.fd(side_length)
    turtle.lt(angle)

# to not let the screen exit
turtle.mainloop()
