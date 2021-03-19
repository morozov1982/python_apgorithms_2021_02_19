"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""
from random import uniform

SIZE = 10  # 100_000
FIRST = 0
LAST = 50


# разбивает список
def split_list(data):
    half = len(data) // 2
    lst1 = data[:half]
    lst2 = data[half:]
    return lst1, lst2


# собирает список
def merge_list(lst1, lst2):
    res = []

    while len(lst1) > 0 and len(lst2) > 0:
        if lst1[0] < lst2[0]:
            res.append(lst1.pop(0))
        else:
            res.append(lst2.pop(0))

    return res + lst1 + lst2


def merge_sort(data):
    if len(data) < 1:
        return data

    lst1, lst2 = split_list(data)

    if len(lst1) > 1:
        lst1 = merge_sort(lst1)
    if len(lst2) > 1:
        lst2 = merge_sort(lst2)

    return merge_list(lst1, lst2)


arr = [uniform(FIRST, LAST) for _ in range(SIZE)]
print(f'\33[92m\33[1mМассив:\33[0m')
print(arr)


arr = merge_sort(arr)
print(f'\n\33[92mОтсортированный \33[1mметодом слияния:\33[0m')
print(arr)
