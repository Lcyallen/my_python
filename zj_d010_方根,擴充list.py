while 1:
    try:
        a = int(input())
        factor = []
        for i in range(2,int(a**0.5)+1):    #1.
            if a%i==0 and i!=(a**0.5):      #2.
                factor.append(i)
                factor.append(a//i)
            elif a%i==0 and i==(a**0.5):    #3.
                factor.append(i)
        if 1+sum(factor) == a:
            print("完全數")
        elif 1+sum(factor) > a:
            print("盈數")
        else:
            print("虧數")
    except:
        break
'''
1.因為不想檢查到a，所以檢查到根號a，(記得要+1)
2.如果沒有分兩種情況，遇到a是完全平方數時，會加兩次因數，使因數和增加
3.若遇到完全平方數，檢查到平方根的因數時，a//i就不用再指派進factor[]裡了
4. i是int, a**0.5是float，但兩數仍可比大小