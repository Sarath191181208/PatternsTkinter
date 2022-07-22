import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
t.speed(20)
h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 0.7, 0.7)
    h += 1/360
    t.color(c)
    t.circle(180)
    t.left(10)
