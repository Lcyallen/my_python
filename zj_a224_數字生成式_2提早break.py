while 1:
    try:
        a = input().lower() #看網路高手寫的，此時a仍為str
#        lower = a.lower() #把a字串的字母都變成小寫字母
        index = [int('0')]*26 #不能寫成index = [], 這是表示index是"空"list而不是0
        for i in a:
            if i.isalpha() == True:
                index[ord(i)-ord('a')] += 1
        count = 0
        for j in range(26):
            if index[j]%2 != 0:
                count += 1
                if count == 2:  #一旦字母數量有2個奇數個，就一定不是迴文
                    print("no...")
                    break
        if count < 2:   #py沒有return 0, 所以必須再判斷一次
            print("yes !")
    except:
        break
#這樣的寫法快了1ms
'''
1.因為index的寫法錯誤而卡關很久，這是要注意的地方        
2.如果寫成index = ['0']*26則'0'為str而非int，所以要再強制轉換變數型態
'''