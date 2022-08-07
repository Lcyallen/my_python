t = int(input())
for i in range(t):  #確定以下事情要做t次，用for+range(t)
    a = int (input())
    if a ==0:       #原本沒有考慮輸入為0的情況，後來看cpp檔案才發現
        print (0)
    else:
        product = 1
        while a:
            product *= a%10
            a //= 10
        print(product)

#原本一直想利用try...except來寫，但還沒試成功