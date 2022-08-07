while 1:
    try:
        a, b = map(int, input().split())
        sum = a     #刻意讓sum一開始就=a
        d = 1       #此時已經算數了第一個數
#        for i in range (a+1, sum > b): //到何時停止不能這樣寫？
        while sum <= b:    #判斷如果sum不大於b
            a += 1          #a要到下一個數
            sum += a        #sum累加
            d += 1          #幾個數要再加1
            
        print (d)
    except:
        break