import turtle as t
import colorsys as cs

t.speed(0)
t.width(2)
t.bgcolor('black')

for i in range(150):
    t.circle(50)
    t.right(4)
    t.color(cs.hsv_to_rgb(i/150,0.8,0.8))
    t.fd(1)    #往前1格變得很重要
    
t.done()
