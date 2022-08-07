def g (n):      #此題明顯寫成遞迴函數較方便
    if n == 1:
        return 1
    else:
        return f(n)+g(n-1)

def f (n):      #原本f沒有寫成函數, 但g在呼叫時不方便
    return int((1/2)*(n*(n+1)))
    
while 1:
    try:
        n = int(input())
        print (f(n),g(n))
    except:
        break

#############改成下面的寫法也沒過(NA)
def g (n):      #此題明顯寫成遞迴函數較方便
    if n == 1:
        return 1
    else:
        return f(n)+g(n-1)

def f (n):      #原本f沒有寫成函數, 但g在呼叫時不方便
    if n == 1:
        return 1
    else:
        return n+f(n-1)
    
while 1:
    try:
        n = int(input())
        print (f(n),g(n))
    except:
        break        