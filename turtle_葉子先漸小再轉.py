import turtle as t
import colorsys as cs

t.speed(0)
t.bgcolor('black')

for j in range (20):
    for i in range (10):
        t.color(cs.hsv_to_rgb(j/20,1,1))
        t.circle(160-i*5,90)
        t.left(90)
        t.circle(160-i*5,90)
        t.left(90)
    t.right(90)
    t.circle(25,18)
    t.right(90)
    
t.done()
