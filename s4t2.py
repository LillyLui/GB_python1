#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("Задайте натуральное число N: "))
i = 2
lst = []
num = n
while i <= n:
    if n % i == 0:
        lst.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {num} : {lst}")

#проверка
mult = 1
for i in range(len(lst)):
    mult *= lst[i]
print(mult)
