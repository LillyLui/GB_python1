#  Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random
n = int(input("Введите число: "))
lst = [random.randint(-n, n+1) for i in range(0, n)]
print(lst)

mult = 1
poz = open('file_task4', 'r')

for line in poz:
    if int(line) < n:
        mult *= lst[int(line)]
poz.close()
print(mult)