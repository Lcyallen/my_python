import turtle as t
import colorsys as cs
import time

t.speed(0)
t.bgcolor('black')
t.width(4)

l = 100
def Square (l):
    t.lt(45)
    for i in range (3):
        t.fd(l)
        t.lt(90)
for j in range (10):
    for i in range (10):
        t.color(cs.hsv_to_rgb(i/10,0.9,1))
        Square (l)
        t.fd(l)
        t.rt(135)
        t.circle(25,36)
        t.rt(180)
    l -= 1
#print(t.heading())
        
time.sleep(2)
