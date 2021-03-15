# Предположу, что об этом шла речь в конце вебинара
# https://habr.com/ru/company/mailru/blog/202832/
from memory_profiler import profile


# pip3 install psutil memory_profiler
# python3 -m memory_profiler task_1_1.py
@profile
def func_1(arr):
    second = []

    for idx, num in enumerate(arr):
        if not num % 2:
            second.append(idx)


lst = [31, 94, 99, 75, 12, 58, 4, 5, 94, 25]
func_1(lst)

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#      8     18.0 MiB     18.0 MiB           1   @profile
#      9                                         def func_1(arr):
#     10     18.0 MiB      0.0 MiB           1       second = []
#     11
#     12     18.0 MiB      0.0 MiB          11       for idx, num in enumerate(arr):
#     13     18.0 MiB      0.0 MiB          10           if not num % 2:
#     14     18.0 MiB      0.0 MiB           5               second.append(idx)


@profile
def func_2(arr):
    second = tuple(idx for idx, num in enumerate(arr) if num % 2 == 0)


tpl = (31, 94, 99, 75, 12, 58, 4, 5, 94, 25)
func_2(tpl)

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     32     18.0 MiB     18.0 MiB           1   @profile
#     33                                         def func_2(arr):
#     34     18.0 MiB      0.0 MiB          18       second = tuple(idx for idx, num in enumerate(arr) if num % 2 == 0)


@profile
def func_3(arr):
    tuple(arr[i] for i in arr.keys() if arr[i] % 2 == 0)


dct = {0: 16, 1: 22, 2: 45, 3: 95, 4: 76, 5: 89, 6: 60, 7: 2, 8: 13, 9: 25}
func_3(dct)

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     46     18.0 MiB     18.0 MiB           1   @profile
#     47                                         def func_3(arr):
#     48     18.0 MiB      0.0 MiB          18       tuple(arr[i] for i in arr.keys() if arr[i] % 2 == 0)

"""
Не до конца понял как им пользоваться и на что смотреть,
надеюсь на вебинаре что-то прояснится.
"""
