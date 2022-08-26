n = int(input())
for j in range(n):  #若用i最後印出時會有問題
    a = int(input())
    b = int(input())
    sum = 0
    for i in range(a,b+1):
        if i%2:
            sum += i
    print(f'Case {j+1}: {sum}')