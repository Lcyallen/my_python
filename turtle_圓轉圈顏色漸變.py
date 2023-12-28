import turtle as t
import colorsys as cs
import time

t.speed(0)
t.width(2)
t.bgcolor('black')

for i in range(100):
    t.circle(50)
    t.right(4)
    t.color(cs.hsv_to_rgb(i/100,1,0.8))
    
time.sleep(2)