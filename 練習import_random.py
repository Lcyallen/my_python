import random
a =[]
for i in range(3):
    a.append(random.randint(0,20))
for i in a:
    print(i,end=' ')
print()
print(max(a))
print(min(a))
print(sum(a))