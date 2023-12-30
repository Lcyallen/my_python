import turtle as t
import colorsys as cs
import time

t.speed(0)
t.width(2)
t.bgcolor('black')

for i in range(100):
    t.right(90)
    t.color(cs.hsv_to_rgb(i/100,0.9,0.8))
    t.circle(200-i*0.5,90)
    t.left(90)
    t.circle(200-i*0.5,90)
    t.right(180)  #轉180度才能畫同一個圓
    t.circle(25,24)

time.sleep(5)