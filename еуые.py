'''Пусть M(k) = 7 000 000 + k, где k – натуральное число.
Найдите пять наименьших значений k, при которых M(k) нельзя представить
в виде произведения трёх различных натуральных чисел, не равных 1.
В ответе запишите найденные значения k в порядке возрастания.'''

from itertools import *

def dvx(x): return set([d for d in range(2,int(x**0.5)+1) if x%d==0]+[x//d for d in range(2,int(x**0.5)+1) if x % d == 0])

cnt = 0
n = 7_000_000
i = 1
while cnt != 5:
    n += 1
    f = True
    if len(dvx(n)) < 3:
        print(i)
        cnt += 1
    else:
        for j in combinations(dvx(n), 3):
            if j[0] * j[1] * j[2] == n:
                f = False
                break
        if f:
            print(i)
            cnt += 1
    i += 1