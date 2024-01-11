import turtle as t
import colorsys as cs

t.speed(0)
t.bgcolor('black')

for j in range (15):
    for i in range (8):
        t.color(cs.hsv_to_rgb(i/8,1,1))
        t.circle(150-i*5,90)
        t.lt(90)
        t.circle(150-i*5,90)
        t.lt(90)    #左轉90度才能回原方向繼續畫葉子
    t.rt(180)   #畫完葉子方向向右，此時須先向後轉，往左前進
    t.circle(25,24) #走小圈
    t.rt(180)   #這個是關鍵！
t.done()
