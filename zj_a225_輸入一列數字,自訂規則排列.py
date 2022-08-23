while 1:
    try:
        n = int(input())
        a = [int(i) for i in input().split(' ')]
#        a.sort(reverse = True)
#        print(a)
        for i in range(n):
            for j in range (i+1, n):
                if a[j]%10<a[i]%10 or a[j]%10==a[i]%10 and a[j]>a[i]:
                    a[j], a[i] = a[i], a[j]
        for k in range(n):
            print (a[k], end=' ')                
        print ()
    except:
        break
'''
1.這是我參考cpp的內容才寫出來的
2. if的判斷式必須寫在同一個位階才能跑出正確答案，如果寫成兩個for, 就錯誤
3.高手寫法https://steam.oxxostudio.tw/category/python/zerojudge/a225.html