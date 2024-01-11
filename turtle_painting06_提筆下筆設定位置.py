import turtle as t

t.color('blue')
t.width(2)
t.speed(5)

print('要畫幾星星?')
n = int(input())

t.penup()
t.goto(-150,150)

for j in range(n):
  for i in range(5):
    t.pendown()
    t.fd(20)
    t.rt(144)
  t.penup()
  t.forward(40)
    
t.done()
