import turtle as t

#t.speed()
t.penup()
t.goto((-200, 50))
t.pendown()
  

def star(size):
    if size <= 50:
        return
    else:
        for i in range(5):
            t.forward(size)
            star(size/3)
            t.rt(144)
  
star(180)

t.done()