import turtle as t
import colorsys as cs
import time

t.speed(0)
t.bgcolor('black')

for i in range (60):
    t.color(cs.hsv_to_rgb(i/60,1,1))
    t.width(i*0.05)
    t.rt(110)
    t.fd(i*1.5)
    t.rt(40)
    t.bk(i*3)
    t.circle(60,90)
        
#print(t.heading()) #可以獲得目前的方向角

time.sleep(2)
