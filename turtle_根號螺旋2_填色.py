import turtle as t

colors = ['sky blue','blue','Indigo','purple','pink','red','brown','gold','yellow','orange','green','light green']
t.speed(0)
x, y = 50, 0
for i in range (16):
    t.fillcolor(colors[i%12])
    t.begin_fill()
    ang = t.towards(x,y)    #1.把角度算出來
    t.setheading(ang)   #2.讓t面向這個方向
    t.goto(x,y)     #3.走到定位
    t.lt(90)
    t.fd(50)
    x, y = t.pos()
    t.goto(0,0)
    t.end_fill()

t.done()