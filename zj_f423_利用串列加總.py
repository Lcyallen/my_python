n = int(input())
a = [int(i) for i in range(1,n+1)]  #把1~n+1的數寫入串列
print(sum(a[::2]))  #利用sum()函數把串列中的間隔元素加總