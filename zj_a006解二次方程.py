a,b,c = map(int,input().split())    #三個變數的逗號間竟然不能有空格！
D = b*b-4*a*c
if D>0:
  x1 = int((D**(0.5)-b)//2)      #要注意利用**(0.5)求平方根後，會變成float，要再轉變成int
  x2 = int((0-(D**(0.5))-b)//2)
  print("Two different roots x1=",x1," , x2=",x2,sep='')

elif D==0:
  print("Two same roots x=",(0-b)//(2*a),sep='')    #印出來的結果之間用逗號連接，再用sep=''刪掉空格

else:
  print("No real root")
