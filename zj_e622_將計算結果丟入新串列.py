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
for i in range(n):
    if a[i]==max(a):        #雖然py可以很快找到串列最大值，但要印出idx還是要重新尋找
        print(i+1,end=' ')
print(max(a))        