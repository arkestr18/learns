import random
def printCardName(numCard):
    if numCard==2:
        print('вам выпал валет')
    if numCard==3:
        print('вам выпала дама')
    if numCard==4:
        print('вам выпал король')
    if numCard==6:
        print('вам выпала шестерка')
    if numCard==7:
        print('вам выпала семерка')
    if numCard==8:
        print('вам выпала восьмерка')
    if numCard==9:
        print('вам выпала девятка')
    if numCard==10:
        print('вам выпала десятка')
    if numCard==11:
        print('вам выпал туз')

k = 0
z = 0
while True:
    z +=1
    i=random.randint(2, 11)
    if i==5:
      continue
    printCardName(i)
    k += i
    print(k)
    if k > 21:
        print('вы проиграли')
        break
    if z==6:
        print('максимальное количество карт')
        if k>21:
            print('вы проиграли')
        break
    print('если надо еще введите 1\n если все то введите 2')
    a = int(input())
    if a == 2:
        break
    elif a == 1:
        continue
print('ваша сумма ' + str(k))