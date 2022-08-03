while 1:    #因為本題要求EOF
    try:
        n = int(input())
        a = list(map(int, input().split())) #(1)
        a.sort()
        for i in a:
            print(i,end=' ')
        print()
    except:
        break

#(1)看高手這樣寫：a = [int(i) for i in input().split(' ')]