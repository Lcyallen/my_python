import turtle as t

t.speed(0)
t.bgcolor('black')
t.color('white')
t.width(2)
def Tri (len):
    if len < 10:
        return
    
    for i in range (3):
        t.fd(len)
        t.lt(120)
        Tri(len/2)

t.up()
t.goto(-80,0)
t.down()
Tri(200)
t.done()