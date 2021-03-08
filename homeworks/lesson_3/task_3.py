"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
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

for idx, el in enumerate(array):
    if el > max_el:
        max_el = el
        max_idx = idx
    if el < min_el:
        min_el = el
        min_idx = idx

print(f'Минимальный: {min_el}, индекс: {min_idx}\nМаксимальный: {max_el}, индекс: {max_idx}')

array[min_idx], array[max_idx] = array[max_idx], array[min_idx]
print(array)
