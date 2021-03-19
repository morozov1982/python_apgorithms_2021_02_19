"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""
from random import uniform
import timeit

SIZE = 10  # 1_000_000
FIRST = 0
LAST = 50


# разбивает список
def split_list(data):
    half = len(data) // 2
    lst1 = data[:half]
    lst2 = data[half:]
    return lst1, lst2


# собирает список (старый)
def merge_list_old(lst1, lst2):
    res = []

    while len(lst1) > 0 and len(lst2) > 0:
        if lst1[0] < lst2[0]:
            res.append(lst1.pop(0))  # фу, позор мне за pop()
        else:
            res.append(lst2.pop(0))  # фу, позор мне за pop()

    return res + lst1 + lst2


# собирает список (новый)
def merge_list(lst1, lst2):
    res = []

    len1, len2 = len(lst1), len(lst2)
    i, j = 0, 0

    while len1 > i and len2 > j:
        if lst1[i] <= lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1

    return res + lst1[i:] + lst2[j:]


def merge_sort(data):
    if len(data) < 1:
        return data

    lst1, lst2 = split_list(data)

    if len(lst1) > 1:
        lst1 = merge_sort(lst1)
    if len(lst2) > 1:
        lst2 = merge_sort(lst2)

    return merge_list(lst1, lst2)


def merge_sort_old(data):
    if len(data) < 1:
        return data

    lst1, lst2 = split_list(data)

    if len(lst1) > 1:
        lst1 = merge_sort(lst1)
    if len(lst2) > 1:
        lst2 = merge_sort(lst2)

    return merge_list_old(lst1, lst2)


arr = [uniform(FIRST, LAST) for _ in range(SIZE)]
print(f'\33[92m\33[1mМассив:\33[0m')
print(arr)


arr = merge_sort(arr)
print(f'\n\33[92mОтсортированный \33[1mметодом слияния:\33[0m')
print(arr)


# Проверим, добавилось ли скорости
print(f'\n\33[94mТест скорости для \33[93m\33[1mmerge_sort_old():\33[0m')
print(timeit.timeit('merge_sort_old([uniform(FIRST, LAST) for _ in range(100)])', number=100, globals=globals()))  #
print(timeit.timeit('merge_sort_old([uniform(FIRST, LAST) for _ in range(200)])', number=100, globals=globals()))  #
print(timeit.timeit('merge_sort_old([uniform(FIRST, LAST) for _ in range(400)])', number=100, globals=globals()))  #
print(timeit.timeit('merge_sort_old([uniform(FIRST, LAST) for _ in range(800)])', number=100, globals=globals()))  #
print(timeit.timeit('merge_sort_old([uniform(FIRST, LAST) for _ in range(1600)])', number=100, globals=globals()))  #


print(f'\n\33[94mТест скорости для \33[93m\33[1mmerge_sort():\33[0m')
print(timeit.timeit('merge_sort([uniform(FIRST, LAST) for _ in range(100)])', number=100, globals=globals()))  #
print(timeit.timeit('merge_sort([uniform(FIRST, LAST) for _ in range(200)])', number=100, globals=globals()))  #
print(timeit.timeit('merge_sort([uniform(FIRST, LAST) for _ in range(400)])', number=100, globals=globals()))  #
print(timeit.timeit('merge_sort([uniform(FIRST, LAST) for _ in range(800)])', number=100, globals=globals()))  #
print(timeit.timeit('merge_sort([uniform(FIRST, LAST) for _ in range(1600)])', number=100, globals=globals()))  #
