h, m = [int(i) for i in input().split()]
print("At School" if (h*60+m)>=450 and (h*60+m)<1020 else "Off School")