n = int(input())            # 按照題目先輸入一組數字
for i in range(n):
  a = int(input())          # 輸入第一個數字
  b = int(input())          # 輸入第二個數字
  result = []               # 記錄完全平方數的串列
  for j in range(a, b+1):   # 取出範圍內所有數字
    j2 = j**0.5 * 100       # 開根號後乘以 100
    if j2%100==0:           # 如果除以 100 後沒有餘數
      result.append(j)      # 表示為完全平方數，記錄到 result 裡
  print(f'Case {i+1}: {sum(result)}')  #利用格式化輸出; 利用sum()括號裡放list可以把list裡的數字全加總！
  
  '''
  1.從這裡可以學到善用list，真是厲害！
  2.格式化輸出很聰明