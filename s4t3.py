#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
#исходной последовательности.

lst = []
for num in input("Введите числа через пробел:").split():
    lst.append(int(num))

lst_2 = []
for i in lst:
    if lst.count(i) == 1:
        lst_2.append(i)

print(f"Список неповторяющихся элементов исходной последовательности: {lst_2}")


