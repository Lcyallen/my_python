import turtle as t
t.up()
t.goto(-200,200)
t.down()
#t.speed()

def Triangle (len):
    if len < 8:
        return
    for i in range (3):
        t.fd(len)
        t.rt(120)
    t.fd(len/2)
    t.rt(60)
    Triangle (len/2)

Triangle (400)
t.done()