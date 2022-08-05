def is_prime (k):   #第一次寫py的函數, 要有def 函數名(參數)
    if k == 1:
        return 0    #return值之後就不會再往下執行了
    elif k == 2 or k == 3:
        return 1
    else:
#        c = 0
        for i in range (2,int(k**0.5)+1):   #記得開根號取整數的寫法
            if k%i == 0:
 #               c += 1     #原本想計算<=k 共有幾個因數，後來發現只要有因數就不是質數了！
                return 0
#        if c != 1:
        return 1
#        else:
            #return 1
#print(is_prime (121))
while 1:
    try:
        a, b = map(int, input().split())
        p = []
        for i in range (a, b+1):
            if is_prime (i) == 1:
                p.append (i)        #把i加入p[]中
#for i in p:
        print (len(p))
    except:
        break