#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
#и записать в файл многочлен степени k.

import random
from polin import polynomial


def ind_mn(n):
    lst = [random.randint(0, 100) for i in range(n + 1)]
    return lst


k = int(input("Введите натуральную степень k = "))
k_mn = ind_mn(k)
with open('file_s4t4.txt', 'w') as data:
    data.write(polynomial(k_mn))

