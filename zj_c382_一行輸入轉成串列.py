a = [i for i in input().split()]
if a[1] == '+':
    print(int(a[0])+int(a[2]))
elif a[1] == '-':
    print(int(a[0])-int(a[2]))
elif a[1] == '*':
    print(int(a[0])*int(a[2]))
else:
    print(int(a[0])//int(a[2]))