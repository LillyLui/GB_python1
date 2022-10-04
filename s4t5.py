#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
#содержащий сумму многочленов

from polin import polynomial


def pow_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num


def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num


def ind_mn(mn):
    mn = mn[0].replace(' ', '').split('=')
    mn = mn[0].split('+')
    lst = []
    l = len(mn)
    k = 0
    if pow_mn(mn[-1]) == -1:
        lst.append(int(mn[-1]))
        l -= 1
        k = 1
    i = 1
    ii = l - 1
    while ii >= 0:
        if pow_mn(mn[ii]) != -1 and pow_mn(mn[ii]) == i:
            lst.append(k_mn(mn[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
    return lst


with open('file1_s4t5.txt', 'r') as data:
    mn1 = data.readlines()
with open('file2_s4t5.txt', 'r') as data:
    mn2 = data.readlines()
print(f"Первый многочлен: {mn1}")
print(f"Второй многочлен: {mn2}")
lst1 = ind_mn(mn1)
lst2 = ind_mn(mn2)
print(lst1)
print(lst2)

lst3 = []

if len(lst1) > len(lst2):
    for i in range(len(lst2)):
        lst3.append(lst1[i] + lst2[i])
    for i in range(len(lst2), len(lst1)):
        lst3.append(lst1[i])
else:
    for i in range(len(lst1)):
        lst3.append(lst1[i] + lst2[i])
    for i in range(len(lst1), len(lst2)):
        lst3.append(lst2[i])

print(lst3)


with open('file3_s4t5.txt', 'w') as data:
    data.write(polynomial(lst3))


