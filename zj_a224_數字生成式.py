while 1:
    try:
        a = input()
        lower = a.lower() #把a字串的字母都變成小寫字母
#print (lower)
        index = [int('0')]*26 #不能寫成index = [], 這是表示index是"空"list而不是0
#print (index)
        for i in lower:
            if i.isalpha() == True:
                index[ord(i)-ord('a')] += 1
#print(index)
        count = 0
        for j in range(26):
            if index[j]%2 != 0:
                count += 1
        print("no..." if count > 1 else "yes !")
    except:
        break

'''
1.因為index的寫法錯誤而卡關很久，這是要注意的地方        
2.如果寫成index = ['0']*26則'0'為str而非int，所以要再強制轉換變數型態
'''