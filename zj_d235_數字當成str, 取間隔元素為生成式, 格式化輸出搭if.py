while 1:
    try:
        a = input()
        if a == '0':    #要注意輸入是str
            break
        odd = [int(i) for i in a[::2]]      #如果a是str則可以利用index產生生成式
        even = [int(i) for i in a[1::2]]    #原本想先宣告2個空串列再用append, 後來試生成式成功！
        print(f'{a} is not a multiple of 11.' if (sum(odd)-sum(even))%11 else f'{a} is a multiple of 11.')  #f''+if
    except:
        break