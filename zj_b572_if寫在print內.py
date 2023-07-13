n = int(input())
for i in range(n):
    h1, m1, h2, m2, t = [int(i) for i in input().split()]
    print("No" if (h1*60+m1+t)>(h2*60+m2) else "Yes")