import turtle


def draw_shape(dim, side_length, bl=False):
    """ draws an n dimensional shape"""
    # side_length = 100
    # n = int(input("Enter the n sided polygon you want : "))

    # external angle property
    angle = 180 - ((dim - 2) * 180) / dim
    # dim sided polygon
    for i in range(dim):
        turtle.fd(side_length)
        turtle.lt(angle)


turtle.bgcolor("#000")
turtle.pencolor('SpringGreen2')
turtle.pensize(5)

# Drawing an hexagon
draw_shape(dim=6, side_length=100)

# (15, 15*(3**2))
turtle.up()
turtle.goto(15, 15*(3**(1/2)))
turtle.down()

dim = 6
side_length = 70

# external angle property
angle = 180 - ((dim - 2) * 180) / dim
# dim sided polygon
for i in range(dim):
    if i % 2 == 1:
        turtle.fd(side_length)
        turtle.lt(angle)
    else:
        turtle.up()
        turtle.fd(side_length)
        turtle.lt(angle)
        turtle.down()

# draw_shape(dim=6, side_length=70, bl=True)


turtle.mainloop()
