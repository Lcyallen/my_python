n, s = [int(i) for i in input().split()]
a = []
for i in range(n):
    cp, iv = [int(i) for i in input().split()]
    if iv<30:
        a.append(cp+s//1000*10)  #不能直接寫成s//100,答案會不同
    elif iv>39:
        a.append(cp+s//1000*100)
    else:
        a.append(cp+s//1000*50)
print(a.index(max(a))+1,max(a))     #利用a.index()可以找出第幾個,但記得要+1

#https://vimsky.com/zh-tw/examples/usage/python-list-index.html