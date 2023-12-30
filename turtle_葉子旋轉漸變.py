import turtle as t
import colorsys as cs
import time

t.speed(0)
t.width(2)
t.bgcolor('black')

for i in range(200):
    t.rt(2)
    t.fd(2)            #學網路另一種寫法，確實出現我想要的中心圓，但卻不是我覺得美的效果
    for j in range(2):
        t.right(90)
        t.color(cs.hsv_to_rgb(i/200,0.9,0.8))
        t.circle(200,90)
        t.left(90)
        t.circle(200,90)

time.sleep(5)