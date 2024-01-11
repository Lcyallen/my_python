import turtle as t
import colorsys as cs

t.speed(0)
t.width(2)
t.bgcolor('black')

for i in range(60):
    t.circle(100,90)
    t.lt(90)
    t.circle(100,90)
    t.color(cs.hsv_to_rgb(i/60,0.8,0.8))
    t.circle(10,50)
    
t.done()
