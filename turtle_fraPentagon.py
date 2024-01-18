import turtle as t
t.speed(0)
t.width(2)
t.bgcolor('black')
t.color('white')
def Pentagon (x):
    if x < 8:
        return
    for i in range (5):
        t.fd(x)
        t.lt(72)
        Pentagon(x/2.5)

t.up()
t.goto(-100,-100)
t.down()
Pentagon(200)
t.done()