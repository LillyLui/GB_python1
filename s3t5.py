#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def neg_fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        num1 = 1
        num2 = -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2


lst = []
a = int(input('Введите число: '))
for k in range(1, a + 1):
    lst.append(fib(k))
    lst.insert(0, neg_fib(k))
print(lst)
