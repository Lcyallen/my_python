t = int(input())
for i in range(t):  
    n = int(input())
    x = [int(i) for i in input().split()]
    print((max(x)-min(x))*2)