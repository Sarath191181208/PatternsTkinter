import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
t.speed(0)
h = 0
for j in range(360):
    t.begin_fill()
    for i in range(2):
        c = colorsys.hsv_to_rgb(h, 0.7, 0.7)
        h += 0.01
        t.color(c)
        t.left(20)
        t.forward(j-i)
    t.end_fill()
