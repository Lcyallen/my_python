'''
n = int(input())
while n:
    for i in range(n+1):
        if i%7!=0:
            print(i,end=' ')
'''#這樣寫程式進入無窮迴圈，一直印12341234...
while 1:
    try:
        n = int(input())
        n != 0
        for i in range(n):
            if i%7 != 0:
                print(i,end=' ')
        print()
    except:
        break
#這樣寫當輸入0時程式並沒有結束，只是跳過幾行，仍在等待下個數字輸入
#原本我以為這樣是不行的，但從下面別人的解答發現這樣是可以的！
'''以下是網路高手的解答
while 1:
    try:
        n = int(input())
        for i in range(1, n):
            if i%7 != 0:
                print(i,end=' ')
        print()
    except:
        break
'''
