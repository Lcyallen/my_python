n = int(input())
result = ['a leap year', 'a normal year']   #把要輸出的內容存成串列
for i in range (n):
    y = int(input())
    if y%4==0 and y%100!=0 or y%400==0:
        print(f'Case {i+1}: {result[0]}')   #格式化輸出要多複習
    else:
        print(f'Case {i+1}: {result[1]}')