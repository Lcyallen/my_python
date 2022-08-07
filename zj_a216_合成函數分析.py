while 1:
    try:
        n = int(input())
        f = g = 0
        for i in range (1,n+1):
            f += i
            g += f      #動筆算了一下，g其實是f累加的結果
        print (f, g)
        
    except:
        break
'''
之前寫了2個遞迴都無法通過。
參考高手的寫法，發現不要寫遞迴反而更簡潔，而且AC！
'''        