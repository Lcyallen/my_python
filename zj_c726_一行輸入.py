#1.我自己寫的
'''g, b = map(str, input().split())
print(g,"and",b,"sitting in the tree")
#輸出格式中我忘記加逗號
'''
#2.看別人寫法發現也可以寫成以下:
'''g, b = input().split()
print(g,"and",b,"sitting in the tree")'''

#3.練習格式化輸出,記得在print()內寫f''
g, b = input().split()
#print(f'{g} and {b} sitting in the tree')

#實驗是否可以輸入多個字串
g, b, c = input().split()
print (g, "and" ,b, "and", c)