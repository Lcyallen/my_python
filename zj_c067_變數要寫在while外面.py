k = 0   #這邊想最久！這個變數要寫在while外面，這樣每次重複執行時k值才不會又被歸0
while 1:
    try:
        n = int(input())
        if n == 0:
            break
        hi = [int(i) for i in input().split()]
        m = 0        
        for i in hi:
            if i>(sum(hi)//n):
                m += i-(sum(hi)//n)
        k += 1    
        print(f'Set #{k}')
        print(f'The minimum number of moves is {m}.')
    except:
        break