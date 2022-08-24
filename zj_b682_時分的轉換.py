h1, m1 = [int(i) for i in input().split()]
h2, m2 = [int(i) for i in input().split()]
if h1==h2 and m1>m2:
    print(23, 60+m2-m1)
else:
    print(((h2+24-h1)%24*60+(m2-m1))//60,((h2+24-h1)%24*60+(m2-m1))%60)