a = input()
for i in range(6):  #一開始寫(7)但下面邏輯判斷時無法執行，所以改成(6)
    if ord(a[i])>ord(a[i+1]):
        print(ord(a[i])-ord(a[i+1]),end='')  #每個字元都要以ord()轉成數字
    else:
        print(ord(a[i+1])-ord(a[i]),end='')