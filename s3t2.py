# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

lst = []
for num in input("Введите числа через пробел:").split():
    lst.append(int(num))
print(lst)

if len(lst) % 2 != 0:
    l: int = len(lst)
    n: int = l // 2
else:
    l: int = len(lst)
    n: int = l // 2 + 1

lst2 = []
for i in range(len(lst)):
    while i < n <= l:
        l -= 1
        a = lst[i] * lst[l]
        lst2.append(a)
        i += 1
print(lst2)
