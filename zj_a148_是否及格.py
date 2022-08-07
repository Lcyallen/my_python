while 1:
    try:
        score = list(map(int,input().split()))  #不用在前面寫for, 要記得
        print ("no" if sum(score[1::]) > 59*score[0] else "yes")   #(1)
    except:
        break

#sum(串列)也可以用[]只加部份串列!