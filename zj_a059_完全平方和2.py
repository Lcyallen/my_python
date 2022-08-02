n = int(input())
for j in range(n):
    a = int(input()) #輸入第一個數
    b = int(input()) #輸入第二個數
    sum = 0
    for i in range (a,b+1):
        if int(i**0.5)**2 == i:
            sum += i
#    print(sum)
    print("Case ",j+1,": ",sum,sep='')