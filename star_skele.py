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
    t.left(10)
    for j in range(5):
        t.forward(200)
        t.left(144)
