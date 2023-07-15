n = int(input())
a = [int(i) for i in input().split()]
a.sort()         #把a排序，a的元素位置就改了
#print(a)
b = []           #需要新建一個list b
for i in range(n-1):   #這裡卡最久，range()內一定要改成n-1否則一直說超過範圍
    if a[i] != a[i+1]: b.append(a[i])  #把append()內的值加入a
b.append(a[n-1])                       #要注意a串列的最後一個數必須加進b
print(len(b))
for i in b: print(i,end=' ')