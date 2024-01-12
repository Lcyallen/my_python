import turtle as t

t.fd(50)
t.speed(0)
for i in range (16):
    x, y = 0, 0
    t.lt(90)
    t.fd(50)
    x, y = t.pos()
    t.goto(0,0)
    ang = t.towards(x,y)
    t.setheading(ang)   #這個設定非常重要！
    t.goto(x,y)

t.done()