import turtle as t
import colorsys as cs
import time

t.speed(0)
t.bgcolor('black')

print('輸入幾邊形')
n = int(input())
for i in range (100):
    t.color(cs.hsv_to_rgb(i/100,0.9,0.9))
    t.fd(i*1.3)
    t.width(i/80+1)
    t.rt(360/n-1)

time.sleep(3)    