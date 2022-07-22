import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
t.speed(20)
h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 0.7, 0.7)
    h += 0.01
    t.color(c)
    t.left(2)
    t.forward(i*2)
    t.right(150)
    for j in range(3):
        t.rt(2)
        t.forward(4)
        t.left(150)
