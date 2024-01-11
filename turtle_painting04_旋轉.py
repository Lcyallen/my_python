import turtle as t

colors = ['blue','red','green','yellow','black']  #把顏色寫進list
t.color('black')
t.width(3)   #設定筆寬

for j in range (10):
    for i in range (4):
        t.forward(50)
        t.right(90)
    t.right(36)
    t.color(colors[j%5])
    
t.done()
