while 1:
    try:
        a, b = map(int, input().split())
        n = 1
        while 1:     #讓程式不斷做以下事情
            if n*(2*a+n-1) <= 2*b:      #利用等差級數的和，若還沒超過條件
                n += 1                  #就把n+1繼續跑迴圈
            else:
                print (n)               #否則把n印出來
                break                   #跳出迴圈
    except:
        break