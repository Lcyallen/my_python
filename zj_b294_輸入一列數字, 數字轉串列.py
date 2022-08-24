d = int(input())
n = [int(i) for i in input().split()]   #如果確定輸入一列數字，最快的方式是指派為串列
total = 0
for j in range(d):
    total += (j+1)*n[j]
print(total)