import turtle
import colorsys

clr = ["white", "red", "green", "blue", "pink", "orange"]

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
t.speed(20)
h = 0
for i in range(150):
    t.color(clr[i % 6])
    t.forward(i*1.5)
    t.left(59)
    t.width(3)
