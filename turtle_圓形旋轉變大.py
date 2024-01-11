import turtle as t

t.speed(0)
t.width(2)
colors =['blue','green','red','brown','pink','purple','orange','black']

for i in range(1,8):
    for j in range(1,8):
        t.circle(i*10)
        t.right(45)
    t.color(colors[i%8])

t.done()
