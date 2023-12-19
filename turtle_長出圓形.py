import turtle
import time

t = turtle.Turtle()
t.speed(0)
t.width(2)
colors =['blue','green','red','brown','pink','purple','orange','black']

for i in range(8):
    for j in range(1,10):
        t.circle(j*5)
    t.right(45)
    t.color(colors[i%8])

time.sleep(1)