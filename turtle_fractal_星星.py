import turtle as t
t.bgcolor('#272829')
t.color('#96EFFF')
t.speed(0)
t.penup()
t.goto((-250, 60))
t.pendown()
t.width(2)  

def star(size):
    if size <= 10:
        return
    else:
        for i in range(5):
            t.forward(size)
            t.rt(144)
            star(size/3)
  
star(500)

t.done()