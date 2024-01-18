import turtle as t

t.speed(0)
t.bgcolor('black')
t.color('yellow')
t.width(2)

def Tri (len):
    if len < 9:
        return
    
    for i in range (3):
        t.fd(len)
        t.lt(120)
        Tri(len/2)

t.up()
t.goto(-150,-50)
t.down()
Tri(300)
t.done()