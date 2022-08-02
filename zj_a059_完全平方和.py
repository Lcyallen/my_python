n = int(input())
for j in range(n):
    a = int(input()) #輸入第一個數
    b = int(input()) #輸入第二個數
    end = int(b**(0.5)+1)
    sum = 0
    for i in range (1,end):
        if i*i>=a and i*i<=b:  #這是自己想出來的解套方法
            sum += i*i
    print("Case ",j+1,": ",sum,sep='') #不能用i，會與上面的i搞混