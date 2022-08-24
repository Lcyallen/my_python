y = int(input())
print("a leap year" if y%4==0 and y%100!=0 or y%400==0 else "a normal year")