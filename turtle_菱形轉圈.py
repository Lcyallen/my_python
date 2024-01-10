import turtle as t
import colorsys as cs
import time

t.speed(0)
t.bgcolor('black')

def Diaman(l):
    for i in range (2):
        t.fd(l)
        t.lt(40)
        t.fd(l)
        t.lt(150)
l = 5        
for j in range (96):
    Diaman(l)
    t.width(j*0.02)
    t.rt(20)
    t.color(cs.hsv_to_rgb(j/11,1,1))
    t.circle(50,25)
    t.rt(90)
    l += 1


#print(t.heading()) #可以獲得目前的方向角

time.sleep(2)
