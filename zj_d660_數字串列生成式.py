for j in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    high = low = 0
    for i in range(1,n):
        if a[i]-a[i-1] > 0: high += 1
        if a[i]-a[i-1] < 0: low += 1
    print(f'Case {j+1}: {high} {low}')