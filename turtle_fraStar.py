import turtle as t
t.speed(0)
#t.width(2)
t.bgcolor('black')
t.color('yellow')

def Star (x):
    if x < 20:
        return
    for i in range (5):
        t.fd(x)
        t.rt(144)
        Star(x/4)

t.up()
t.goto(-150,80)
t.down()
Star(400)    

t.done()