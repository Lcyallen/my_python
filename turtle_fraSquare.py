import turtle as t
t.speed(0)
t.bgcolor('black')
t.color('white')
t.width(2)

def fraSquare (len):
    if len < 5:
        return
    for i in range (4):
        t.fd(len)
        t.lt(90)
        fraSquare(len/3)

t.up()
t.goto(-150,-50)
t.down()
fraSquare(200)
t.done()