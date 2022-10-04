def polynomial(s):
    lst = s[::-1]
    write_mn = ''
    if len(lst) < 1:
        write_mn = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                write_mn += f'{lst[i]}x^{len(lst) - i - 1}'
                if lst[i + 1] != 0:
                    write_mn += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                write_mn += f'{lst[i]}x'
                if lst[i + 1] != 0:
                    write_mn += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                write_mn += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                write_mn += ' = 0'
    return write_mn