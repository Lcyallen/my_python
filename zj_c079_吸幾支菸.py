while 1:
    try:
        n, k = [int(i) for i in input().split()]
        total = n
        while n>=k:
            total += n//k
            n = n//k+n%k
        print(total)
    except:
        break