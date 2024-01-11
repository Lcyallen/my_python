import turtle as t
t.speed(0)

colors =['blue','green','red','brown','pink','purple','orange','black']

for i in range(100):
    t.fd(i)
    t.right(59)
    t.width(i/100+1)   #看到網路上寫的這一行！有很棒的效果
    t.color(colors[i%6])
'''
t.penup()
t.fd(80)

for i in range(100):
    t.fd(i)
    t.right(61)
    t.width(i/100+1)
    t.color(colors[i%6])
'''
t.done()
