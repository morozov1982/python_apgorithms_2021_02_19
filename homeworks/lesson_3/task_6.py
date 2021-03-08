"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


min_el = array[0]
max_el = array[0]
min_idx = 0
max_idx = 0
summary = 0

for idx, el in enumerate(array):
    if el > max_el:
        max_el = el
        max_idx = idx
    if el < min_el:
        min_el = el
        min_idx = idx


if min_idx < max_idx:
    for i in array[min_idx + 1: max_idx]:
        summary += i
    print(f'Сумма чисел между {min_el} и {max_el}: {summary}')
else:
    for i in array[max_idx + 1: min_idx]:
        summary += i
    print(f'Сумма чисел между {max_el} и {min_el}: {summary}')
