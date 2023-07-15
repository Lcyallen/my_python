n = 0   #一開始一直把它寫在"while 1"迴圈裡面！
while 1:
    a = input()
    if a == '#': break
    elif a == 'HELLO':
        print(f'Case {n+1}: ENGLISH')
    elif a == 'HOLA':
        print(f'Case {n+1}: SPANISH')
    elif a == 'HALLO':
        print(f'Case {n+1}: GERMAN')
    elif a == 'BONJOUR':
        print(f'Case {n+1}: FRENCH')
    elif a == 'CIAO':
        print(f'Case {n+1}: ITALIAN')
    elif a == 'ZDRAVSTVUJTE':
        print(f'Case {n+1}: RUSSIAN')
    else:
        print(f'Case {n+1}: UNKNOWN')
    n += 1