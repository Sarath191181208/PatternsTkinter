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
    for j in range(2):
        t.left(250)
        t.forward(i*3)
        for _ in range(2):
            t.left(20)
            t.forward(22)
