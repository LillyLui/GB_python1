# Реализуйте алгоритм перемешивания списка.

import random
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_lst = lst.copy()
random.shuffle(new_lst)
print(new_lst)