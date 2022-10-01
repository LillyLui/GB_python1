#Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

n = int(input("Введите число: "))
lst = [round((1+1/i)**i, 3) for i in range(1, n+1)]
sum = 0
for i in range(0, n):
    sum += lst[i]
print(sum)
