import turtle
import colorsys

clr = ["white", "red", "green", "blue", "pink", "orange"]

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
t.speed(0)
h = 0
for i in range(150):
    t.color(clr[i % 6])
    t.circle(190-i/2, 90)
    t.left(90)
    t.circle(190-i/3, 90)
    t.lt(60)
    # t.width(3)
