import turtle as t
colors = ['black','blue','purple','brown','red','orange','gold','green']
t.speed(0)
x, y = 50, 0
t.color('black')
for i in range (16):
    ang = t.towards(x,y)    #1.把角度算出來
    t.setheading(ang)   #2.讓t面向這個方向
    t.goto(x,y)     #3.走到定位
    t.lt(90)
    t.color(colors[i%8])
    t.fd(50)
    t.write("根號"+str(i+2),font=(14))
    x, y = t.pos()
    t.goto(0,0)
    
t.done()