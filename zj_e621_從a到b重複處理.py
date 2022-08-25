n = int(input())
for i in range(n):
    a, b, c = [int(j) for j in input().split()]
    count = 0
    for i in range(a+1,b):
        if i%c != 0:
            print(i,end=' ')    #輸出的結果要以空格隔開
            count += 1
    if count == 0:
        print("No free parking spaces.")
    print() #最後要空一行