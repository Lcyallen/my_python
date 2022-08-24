a, op, b = input().split()  #一開始寫成list卻無法印出a[i]
if op=='+':
    print(int(a)+int(b))
elif op=='-':
    print(int(a)-int(b))
elif op=='*':
    print(int(a)*int(b))
else:
    print(int(a)//int(b))