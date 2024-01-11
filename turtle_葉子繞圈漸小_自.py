import turtle as t
import colorsys as cs

t.speed(0)
t.bgcolor('black')

for j in range (10):
    for i in range (15):
        t.color(cs.hsv_to_rgb(i/15,1,1))
        t.circle(150-j*3,90)
        t.lt(90)
        t.circle(150-j*3,90)
        t.rt(90)
        t.circle(25,24)
        t.rt(180)

t.done()
