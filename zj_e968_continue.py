n = int(input())
a, b, c = [int(i) for i in input().split()]
for i in range (n,0,-1):
    if i==a or i==b or i==c:
        continue
    print("No.",i)