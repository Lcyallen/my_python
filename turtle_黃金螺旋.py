import turtle as t
import colorsys as cs

t.speed()
t.bgcolor('black')

a = 0
b = 1+a

for i in range (11):
    t.color(cs.hsv_to_rgb(i/11,1,1))
    c = a+b
    t.width(i)
    t.circle(c,90)
    a = b
    b = c
    
t.done()
