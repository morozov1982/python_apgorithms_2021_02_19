# Предположу, что об этом шла речь в конце вебинара
# https://habr.com/ru/company/mailru/blog/202832/
from memory_profiler import profile


# pip3 install psutil memory_profiler
# python3 -m memory_profiler task_1_1.py
@profile
def func_1(arr):
    first = arr
    second = []

    for idx, num in enumerate(first):
        if not num % 2:
            second.append(idx)


lst = [31, 94, 99, 75, 12, 58, 4, 5, 94, 25]
func_1(lst)

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#      8     18.0 MiB     18.0 MiB           1   @profile
#      9                                         def func_1(arr):
#     10     18.0 MiB      0.0 MiB           1       first = arr
#     11     18.0 MiB      0.0 MiB           1       second = []
#     12
#     13     18.0 MiB      0.0 MiB          11       for idx, num in enumerate(first):
#     14     18.0 MiB      0.0 MiB          10           if not num % 2:
#     15     18.0 MiB      0.0 MiB           5               second.append(idx)
