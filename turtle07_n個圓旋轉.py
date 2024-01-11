import turtle as t

t.color('brown')
t.width(2)
t.speed(5)
colors = ['red','orange','yellow','green','blue','purple','pink','brown']

#t.penup()
#t.goto(-150,150)

for i in range(20):
    t.circle(50)
    t.right(18)
    t.color(colors[(i+1)%8])
    
t.done()
