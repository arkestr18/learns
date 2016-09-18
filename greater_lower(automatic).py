# больше меньше автоматически
from random import *

r = randint(0, 100)
a=0
b=100
while True:
    k = randint(a, b)
    if k>r:
        print(str(k) + ' большое число')
        b=k

    elif r>k:
        print(str(k) + ' маленькое число')
        a=k
    elif r==k:
        break
print('вы выиграли ' + str(k) + '=' + str(r))