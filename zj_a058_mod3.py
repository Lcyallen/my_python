n = int(input())
mod3 = [0,0,0]

for i in range(n):
    a = int(input())
    if a%3 == 0:
        mod3[0] += 1
    elif a%3 == 1:
        mod3[1] += 1
    else:
        mod3[2] += 1

for i in mod3:
    print(i,end=' ')